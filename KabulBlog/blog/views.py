
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Category
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
# 3:4