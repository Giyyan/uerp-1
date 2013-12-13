from django import template
from django.template.defaulttags import url
from django.template import Node, TemplateSyntaxError
from django.utils import six
from base.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu.html')
def show_menu():
    return {'menu': MenuItem.objects.all()}