# coding=utf-8
from django.conf.urls import patterns, url
from uerp.apps.hr.views import EmployeeDetailView, EmployeeListView


urlpatterns = patterns(
    '',
    url(r'^employers/$', EmployeeListView.as_view(), name="list"),
    url(r'^employers/page(?P<page>\d+)/$', EmployeeListView.as_view(), name="list"),
    url(r'^employers/(?P<slug>[-\w]+)/$', EmployeeDetailView.as_view(), name="detail"),
)