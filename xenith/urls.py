# -- coding: utf-8 --
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

# Enable the admin app
from django.contrib import admin
admin.autodiscover()


sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap
}


def bad(request):
    """ Simulates a server error """
    1 / 0


urlpatterns = patterns('',
    # Redirect the home page to the blog
    #url(r'^$', RedirectView.as_view(url='/blog/'), name="home"),

    # Single-page template views
    url(r'^$',
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),
    url(r'^contact/$',
        TemplateView.as_view(template_name='pages/contact.html'),
        name="contact"),
    url(r'^calendar/$',
        TemplateView.as_view(template_name='pages/calendar.html'),
        name="calendar"),
    url(r'^bookshelf/$',
        TemplateView.as_view(template_name='pages/bookshelf.html'),
        name="bookshelf"),

    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^avatar/', include('avatar.urls')),

    # This is so we can manage our PowerDNS server from within the admin app
    url(r'^powerdns/', include('powerdns_manager.urls')),

    # URLs for the blog
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc', name='xmlrpc'),

    # Simulate a 500 server error
    url(r'^bad/$', bad),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': sitemaps}),
)

urlpatterns += patterns(
    '',
    url(r'^400/$', 'django.views.defaults.bad_request'),
    url(r'^403/$', 'django.views.defaults.permission_denied'),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'django.views.defaults.server_error'),
)
