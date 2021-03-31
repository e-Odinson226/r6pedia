from django.db import models
from django.utils import timezone
from extentions.utils import jalaliazer

class Category(models.Model):
    rank_choices = [
        ('1', "first"),
        ('2', "second"  ),
        ('3', "third"  ),
        ('4', "fourth"  ),
    ]
    title       = models.CharField(max_length=50, verbose_name="تیتر")
    slug        = models.SlugField(unique=True, max_length=40)
    rank        = models.CharField(max_length=1, choices=rank_choices, verbose_name="رده")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی ها"

    def __str__(self):
        return self.title

class Post(models.Model):
    publish_stats_choices = [
        ('p', "published"),
        ('d', "drafted"  ),
    ]
    subject     = models.CharField(max_length=50, verbose_name="تیتر")
    category    = models.ManyToManyField(Category, verbose_name="دسته‌بندی")
    slug        = models.SlugField(unique=True, max_length=40)
    content     = models.TextField(max_length=100000, verbose_name="مطالب")
    img         = models.ImageField(upload_to="images", verbose_name="تصویر")
    wrote       = models.DateTimeField(auto_now_add=True)
    published   = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    updated     = models.DateTimeField(auto_now=True)
    status      = models.CharField(max_length=1, choices=publish_stats_choices, verbose_name="وضعیت")

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست‌ها"

    def __str__(self):
        return self.subject
    
    def j_published(self):
        return jalaliazer(self.published)
    j_published.short_description = "زمان انتشار"

    def str_categories(self):
        return "، ".join([cat.title for cat in self.category.all()])
    str_categories.short_description = "دسته‌بندی"