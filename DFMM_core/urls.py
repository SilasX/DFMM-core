from django.conf.urls import patterns, include, url
from django.contrib import admin

from DFMM_core import views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^test/$', views.tpage),
    url(r'^admin/', include(admin.site.urls)),
)

