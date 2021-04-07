from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag("blog/tags-tmpl/overlay_menu_cats.html")
def overlay_menu():
    context = {
        "categories" : Category.objects.filter(status="pub")
    }
    return context