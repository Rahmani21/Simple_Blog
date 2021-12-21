from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
# Create your models here.

# Category Model

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = HTMLField()
    url = models.CharField(max_length=150)
    image = models.ImageField(upload_to='category/')
    added_date = models.DateTimeField(auto_now=True,null=True)


    # for showing the image in the admin view
    def image_tag(self):
        return format_html('<img src = "/media{}"/ style = "width:40px;height:40px;border_radius:50%">'.format(self.image))
    def __str__(self):
        return self.title

# Post Model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    url = models.CharField(max_length=150)
    categ = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')


    def __str__(self):
        return self.title


