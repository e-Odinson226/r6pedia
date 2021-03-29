from django.urls import path
from .views import( homepage,
                    magazin,
                    post_detail )

app_name = "blog"
urlpatterns = [
    path('', homepage, name="homepage"),
    path('mag/', magazin, name="mag"),
    path('mag/<slug:slug>', post_detail, name="single-post"),
]