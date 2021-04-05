from django.urls import path
from .views import( homepage,
                    blog_main,
                    post_detail )

app_name = "blog"
urlpatterns = [
    path('', homepage, name="homepage"),
    path('blog/', blog_main, name="blog"),
    path('blog/<slug:slug>', post_detail, name="single-post"),
]