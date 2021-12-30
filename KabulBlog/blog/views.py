
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

def home(request):
    # Load all the post from db
    posts  = Post.objects.all()[:11]
    data = {
        'posts':posts
    }
    return render(request,'home.html', data)


def post(request,post_url):
    post=Post.objects.get(url=post_url) 
    print(post)
    return render(request,'posts.html',{})

# 2:31