from django.contrib import admin
from uerp.apps.hr.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('work_email', 'work_phone', )
    ordering = ('resource__name',)
    fieldsets = (
        (None, {
            'fields': ('resource', 'job', 'department')
        }),
        ('Группы', {
            'fields': ('groups',)
        }),
    )
    filter_horizontal = ('groups', )
    search_fields = ['work_email']


admin.site.register(Employee, EmployeeAdmin)