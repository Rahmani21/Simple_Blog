from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import home,post,category,user_login,user_register,user_logout
app_name = 'blog'
urlpatterns = [
   path('',home,name='home'),
   path('blog/<slug:post_url>',post,name="post"),
   path('category/<slug:url>',category, name="category"),
   path('register',user_register,name='register'),
   path('login',user_login,name='login'),
    path('logout/',user_logout, name="logout"),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
