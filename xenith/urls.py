""" Default urlconf for xenith """

from django.conf.urls import include, patterns, url
from django.contrib import admin
admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^powerdns/', include('powerdns_manager.urls')),
    url(r'^bad/$', bad),
    url(r'', include('base.urls')),
)
