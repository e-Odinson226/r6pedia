from django.shortcuts import render, get_object_or_404
from .models import Post

def homepage(request):
    return render(request, "blog/homepage.html")

def magazin(request):
    posts= Post.objects.filter(status="p").order_by("-published")
    context = {
        "posts" : posts
    }
    return render(request, "blog/magazin.html", context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='p')
    context = {
        "post" : post
    }
    return render(request, "blog/single-post.html", context)