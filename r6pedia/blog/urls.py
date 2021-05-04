from django.urls import path
from .views import( Homepage,
                    Blog,
                    PostDetail,
                    category )

app_name = "blog"
urlpatterns = [
    path('home/', Homepage.as_view(), name="homepage"),
    path('', Blog.as_view(), name="blog"),
    path('blog/<slug:slug>', PostDetail.as_view(), name="single-post"),
    path('category/<slug:slug>', category, name="category"),
]