from django.views.generic import ListView
from uerp.apps.hr.models import Employee


class EmployeeList(ListView):
    model = Employee
    template_name = 'index.html'
    queryset = Employee.objects.prefetch_related('job', 'department', 'resource').order_by('resource__name')
    # queryset = Employee.objects.prefetch_related('job', 'department', 'resource').filter(resource__active=True).order_by('resource__name')
    # queryset = Employee.objects.order_by('resource__name')