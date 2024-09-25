from django.contrib import admin
from .models import Category, Tag, Article, Contact
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_active', 'created_at')
    readonly_fields = ('views',)
    prepopulated_fields = {'slug': ['title']}
    
    
    filter_horizontal = ('tags',)
    list_editable = ('category', 'is_active',)
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')