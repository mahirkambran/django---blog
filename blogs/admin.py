from django.contrib import admin
from .models import Category
from .models import Blog, Comment

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category__category_name', 'author', 'status', 'is_featured', 'created_at')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('status', 'is_featured')


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)

