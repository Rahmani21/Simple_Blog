
from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Post,Category
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import PostForm,CategoryForm
# Create your views here.

def home(request):
    # Load all the post from db
    posts  = Post.objects.all()
    category = Category.objects.all()


    data = {
        'posts':posts,
        'cats': category
    }
    return render(request,'home.html', data)

def addpost(request):
    category = Category.objects.all()
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Post has beed added successully')
            return redirect('blog:home')

        else:
            form = PostForm()
    
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     url = request.POST.get('url')
    #     categ = request.POST.get('categ')
    #     image = request.FILES.get('image')
    #     post = Post(title = title, 
    #         content = content,
    #         url = url,
    #         categ = categ,
    #         image = image
    #     )
    #     post.save()
    #     messages.success(request,'Post has beed added successully')
    #     return redirect('blog:home')
    return render(request, 'add_post.html', {'form':form,'category':category})

def post(request,post_id):
    post=Post.objects.get(post_id=post_id)
    category = Category.objects.all()
    context = {
        'post':post,
        'cats': category
    }
    return render(request,'posts.html',context)



def category(request,cat_id):
    categ = Category.objects.get(cat_id=cat_id)
    posts = Post.objects.filter(categ = categ)
    context = {
        'category': categ,
        'posts': posts
    }
    return render(request,'category.html',context)

def add_category(request):
    form = CategoryForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Post Added Successfully!')
            return redirect('blog:home')
        else:
            form = CategoryForm()
    return render(request,'add_category.html',{'form':form})

def update_category(request,cat_id):
    category = Category.objects.get(cat_id = cat_id)
    form = CategoryForm(request.POST or None,request.FILES, instance=category)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Category update successfully')
            return redirect('blog:home')
        else:
            form = CategoryForm()
    return render(request,'update_category.html',{'form':form})
    

def deleteCategory(request,cat_id):
    category = Category.objects.get(cat_id = cat_id)
    category.delete()
    messages.success(request,"Category has been deleted")
    return redirect('blog:home')
    
def user_register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.warning(request,"Password does not match")
            return redirect('blog:register')
        elif User.objects.filter(username=username).exists():
            messages.warning(request,"Username already taken")
            return redirect('blog:register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,"Email already taken")
            return redirect('blog:register')
        else:
            user = User.objects.create_user(
            first_name = firstname,
            last_name = lastname,
            username= username,
            email = email,
            password = password1,
            )
            user.save()
            messages.success(request,'User has been registered successully')
            return redirect('blog:login')
    return render(request,'register.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        # the fist username and password comming from the database
        if user is not None:
            login(request,user)
            return redirect('blog:home')
        else:
            messages.warning(request,"Invalid username or password")
            return redirect('blog:login')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect("blog:home")

