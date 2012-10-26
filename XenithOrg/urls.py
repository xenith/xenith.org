""" Default urlconf for XenithOrg """

from django.conf import settings
from django.conf.urls.defaults import include, patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    url(r'', include('XenithOrg.base.urls')),
    url(r'^blog/', include('XenithOrg.blog.urls')),
    url(r'^accounts/', include('XenithOrg.accounts.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('debug_toolbar_user_panel.urls')),
    url(r'^bad/$', bad),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
