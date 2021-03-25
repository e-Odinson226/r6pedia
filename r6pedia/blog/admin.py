from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("subject", "content", "published", "status")
    list_filter = ("status", "published")
    search_fields = ("subject", "content")
    prepopulated_fields = {"slug":("subject",)}
    ordering = ["-status", "-published"] 
admin.site.register(Post, PostAdmin)