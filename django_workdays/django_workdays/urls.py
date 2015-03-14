from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url('^quarter/', include('quarter.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
