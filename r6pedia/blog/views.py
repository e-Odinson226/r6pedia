from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

def about(request):
    return render(request, "blog/about.html")
#--------------------------------------------------------------------

class Homepage(ListView):
    template = "blog/homepage.html"
    def get(self, request, *args, **kwargs):
        return render(request, "blog/homepage.html")
""" 
def homepage(request):
    return render(request, "blog/homepage.html") """
#--------------------------------------------------------------------

class Blog(ListView):
    queryset = Post.objects.published()
    paginate_by = 3
    template_name = "blog/blog_main.html"
    context_object_name = "posts"

""" def blog_main(request):
    posts = Post.objects.published()
    paginator = Paginator(posts, 3)
    page = request.GET.get("page")
    page_posts = paginator.get_page(page)
    context = {
        "posts" : page_posts
    }
    return render(request, "blog/blog_main.html", context) """
#--------------------------------------------------------------------

class PostDetail(DetailView):
    template_name = "blog/single-post.html"
    context_object_name = "post"
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug, status='p')
"""         
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='p')
    context = {
        "post" : post
    }
    return render(request, "blog/single-post.html", context) """
#--------------------------------------------------------------------

class CategoryList(ListView):
    paginate_by = 3
    template_name = "blog/category.html"
    
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.posts.published()
    
    def get_context_data(self, **kwargs):
        slug = self.kwargs.get("slug")
        category = get_object_or_404(Category.objects.active(), slug=slug)
        context = super().get_context_data(**kwargs)
        context['category'] =  category
        return context


""" def category(request, slug):
    categories = get_object_or_404(Category, slug=slug, status="pub")
    #posts = categories.posts.published()

    try:
        posts = categories.posts.published()
    except Exception:
        raise Http404

    paginator = Paginator(posts, 3)
    page = request.GET.get("page")
    page_posts = paginator.get_page(page)

    context = {
        "category" : categories,
        "posts" : page_posts,
    }
    return render(request, "blog/category.html", context) """
#--------------------------------------------------------------------