from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import home,post,category,user_login,user_register,user_logout,addpost,add_category,update_category,deleteCategory
app_name = 'blog'
urlpatterns = [
   path('',home,name='home'),
   path('addpost/',addpost, name='addpost'),
   path('addcat/',add_category, name='addcat'),
   path('blog/<int:post_id>',post,name="blog"),
   path('category/<int:cat_id>',category, name="category"),
   path('update_category/<int:cat_id>',update_category, name="update_category"),
   path('delete_category/<int:cat_id>',deleteCategory, name="delete_category"),
   path('register',user_register,name='register'),
   path('login',user_login,name='login'),
   path('logout/',user_logout, name="logout"),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
