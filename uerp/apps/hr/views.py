# coding=utf-8
from urllib.parse import urlparse
from django.views.generic import ListView, DetailView, RedirectView
from uerp.apps.hr.models import Employee

from django.conf import settings
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, login, authenticate,
    logout)
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from .forms import LoginForm


class LoginView(FormView):
    form_class = LoginForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'users/login.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(work_email=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('login'))

    def get_success_url(self):
        if self.success_url:
            redirect_to = self.success_url
        else:
            redirect_to = self.request.REQUEST.get(self.redirect_field_name, '')

        netloc = urlparse(redirect_to)[1]
        if not redirect_to:
            redirect_to = settings.LOGIN_REDIRECT_URL
        elif netloc and netloc != self.request.get_host():
            redirect_to = settings.LOGIN_REDIRECT_URL
        return redirect_to

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(RedirectView):
    url = '/'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(LogoutView, self).get(*args, **kwargs)


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    # queryset = Employee.objects.prefetch_related('job', 'department', 'resource').order_by('resource__name')
    queryset = Employee.objects.prefetch_related('job', 'department', 'resource').filter(resource__active=True).order_by('resource__name')
    # queryset = Employee.objects.order_by('resource__name')
    paginate_by = 80


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'
