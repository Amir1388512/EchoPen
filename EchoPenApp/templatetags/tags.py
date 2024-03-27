from django import template
from ..models import *  # Import only the necessary model

register = template.Library()

@register.simple_tag
def user_num():
    return User.objects.all().count()

@register.simple_tag
def article_num():
    return Article.objects.all().count()
