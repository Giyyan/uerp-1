import autocomplete_light
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

from uerp.apps.ppc.views import PPCDayReport
from uerp.apps.hr.views import LoginView, LogoutView
from uerp.settings.common import MEDIA_ROOT, MEDIA_URL

autocomplete_light.autodiscover()
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url='/ppc/')),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    
    url(r'^ppc/$', PPCDayReport.as_view()),
    url(r'^hr/', include('uerp.apps.hr.urls', namespace='hr')),
)

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
