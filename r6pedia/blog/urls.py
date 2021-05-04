from django.urls import path
from .views import( Homepage,
                    Blog,
                    post_detail,
                    category )

app_name = "blog"
urlpatterns = [
    path('home/', Homepage.as_view(), name="homepage"),
    path('', Blog.as_view(), name="blog"),
    path('blog/<slug:slug>', post_detail, name="single-post"),
    path('category/<slug:slug>', category, name="category"),
]