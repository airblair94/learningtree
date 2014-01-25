from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    url(r'^index/$', home),
    # url(r'^blog/', include('blog.urls')),
    url(r'^node/$', node),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
