from functools import reduce
from django import template
import operator
from uerp.apps.base.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context, parent=None):
    if parent is None:
        menus = MenuItem.objects.all()
    else:
        menus = MenuItem.objects.filter(parent=parent)
    return {'menu': menus, 'user': context['user']}


@register.assignment_tag()
def menu_perm(menu_item, user):
    if user:
        menus = menu_item.get_descendants(include_self=True)
        users = [u for m in menus for u in m.users.all()]
        groups = [g for m in menus for g in m.groups.all()]
        if user in users or user.groups in groups or user.is_superuser or user.is_staff or user.is_admin:
            return True
    return False