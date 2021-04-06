from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def about(request):
    return render(request, "blog/about.html")
#--------------------------------------------------------------------

def homepage(request):
    categories = Category.objects.filter(status="pub")
    context = {
        "categories" : categories,
    }
    return render(request, "blog/homepage.html", context)
#--------------------------------------------------------------------

def blog_main(request):
    posts = Post.objects.filter(status="p").order_by("-published")
    categories = Category.objects.filter(status="pub")
    context = {
        "categories" : categories,
        "posts" : posts
    }
    return render(request, "blog/blog_main.html", context)
#--------------------------------------------------------------------

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='p')
    context = {
        "post" : post
    }
    return render(request, "blog/single-post.html", context)
#--------------------------------------------------------------------