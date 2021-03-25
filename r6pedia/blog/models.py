from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    publish_stats_choices = [
        ('p', "published"),
        ('d', "drafted"  ),
    ]
    subject         = models.CharField(max_length=50)
    slug            = models.SlugField(unique=True, max_length=40)
    content         = models.TextField(max_length=100000)
    img             = models.ImageField(upload_to="images")
    write_date      = models.DateTimeField(auto_now_add=True)
    publish_date    = models.DateTimeField(default=timezone.now)
    update_date     = models.DateTimeField(auto_now=True)
    publish_stat    = models.CharField(max_length=1, choices=publish_stats_choices)
