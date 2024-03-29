from django.contrib import admin
from .models import Category,Post

# Register your models here.

# for congfiguration of CategoryAdmin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',"description",'url',"added_date")
    search_fields = ("title",)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', "content", 'url')
    search_fields = ("title",)
    list_filter = ('categ',)
    list_per_page = 50



admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)