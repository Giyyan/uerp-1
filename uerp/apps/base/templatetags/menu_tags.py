from django import template
from django.template.defaulttags import url
from django.template import Node, TemplateSyntaxError
from django.utils import six
from uerp.apps.base.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu.html')
def show_menu(parent=None):
    if parent is None:
        menus = MenuItem.objects.all()
    else:
        menus = MenuItem.objects.filter(parent=parent)
    return {'menu': menus}