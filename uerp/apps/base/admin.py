from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from uerp.apps.base.models import MenuItem


class MenuItemAdmin(DjangoMpttAdmin):
    tree_auto_open = 0
    list_display = ('name', 'url')
    ordering = ('name',)


admin.site.register(MenuItem, MenuItemAdmin)