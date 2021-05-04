from django.urls import path
from .views import( Homepage,
                    blog_main,
                    post_detail,
                    category )

app_name = "blog"
urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    path('blog/', blog_main, name="blog"),
    path('blog/<slug:slug>', post_detail, name="single-post"),
    path('category/<slug:slug>', category, name="category"),
]