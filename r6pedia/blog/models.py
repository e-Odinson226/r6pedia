from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    publish_stats_choices = [
        ('p', "published"),
        ('d', "drafted"  ),
    ]
    subject     = models.CharField(max_length=50, verbose_name="تیتر")
    slug        = models.SlugField(unique=True, max_length=40)
    content     = models.TextField(max_length=100000, verbose_name="مطالب")
    img         = models.ImageField(upload_to="images", verbose_name="تصویر")
    wrote       = models.DateTimeField(auto_now_add=True)
    published   = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    updated     = models.DateTimeField(auto_now=True)
    status      = models.CharField(max_length=1, choices=publish_stats_choices, verbose_name="وضعیت")

    def __str__(self):
        return self.subject
