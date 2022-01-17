
from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Post,Category
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
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


def post(request,post_url):
    post=Post.objects.get(url=post_url)
    category = Category.objects.all()
    context = {
        'post':post,
        'cats': category
    }
    return render(request,'posts.html',context)



def category(request,url):
    categ = Category.objects.get(url=url)
    posts = Post.objects.filter(categ = categ)
    context = {
        'category': categ,
        'posts': posts
    }
    return render(request,'category.html',context)

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

