from django.conf.urls import patterns, include, url
from django.contrib import admin
from ppc.views import PPCDayReport
from res.views import EmployeeList

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', EmployeeList.as_view()),
    url(r'^ppc/$', PPCDayReport.as_view())
)
