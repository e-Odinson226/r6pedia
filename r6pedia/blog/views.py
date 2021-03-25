from django.shortcuts import render
from .models import Post

def homepage(request):
    posts= Post.objects.filter(status="p").order_by("-published")
    context = {
        "posts" : posts
    }
    return render(request, "blog/homepage.html", context)