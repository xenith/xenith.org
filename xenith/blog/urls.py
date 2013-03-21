from django.conf.urls.defaults import *


urlpatterns = patterns('XenithOrg.blog.views',
    url(r'^$', 'index', name='index'),
)
