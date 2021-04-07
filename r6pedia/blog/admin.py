from django.contrib import admin
from .models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "rank", "status")
    list_filter = (["rank"])
    search_fields = (["title"])
    prepopulated_fields = {"slug":("title",)}
    ordering = ["-rank"] 
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ("subject", "content", "j_published", "str_categories", "status")
    list_filter = ("status", "published")
    search_fields = ("subject", "content")
    prepopulated_fields = {"slug":("subject",)}
    ordering = ["-status", "-published"] 
admin.site.register(Post, PostAdmin)