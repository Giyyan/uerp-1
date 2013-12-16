from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from uerp.apps.ppc.views import PPCDayReport
from uerp.apps.hr.views import EmployeeList
from uerp.settings.common import MEDIA_ROOT, MEDIA_URL


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', EmployeeList.as_view()),
    url(r'^ppc/$', PPCDayReport.as_view()),
)

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
