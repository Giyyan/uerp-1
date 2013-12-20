from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from uerp.apps.base.models import MenuItem


class MenuItemAdmin(DjangoMpttAdmin):
    tree_auto_open = 0
    list_display = ('name', 'url')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'url', 'parent')
        }),
        ('Доступы', {
            'fields': (('users', 'groups'),)
        }),
        ('Дополнительные настройки', {
            'classes': ('collapse',),
            'fields': ('order',)
        }),
    )
    filter_horizontal = ('groups', 'users',)
    search_fields = ['name', 'url', 'parent']


admin.site.register(MenuItem, MenuItemAdmin)