from django.conf.urls import patterns, url
import blog.views

urlpatterns = patterns('blog.views',
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<pk>\d+)-(?P<slug>.+)/$', blog.views.ArticleView.as_view(), name='article-detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', blog.views.ArticleListView.as_view(), name='article-list-by-month'),
    url(r'^(?P<year>\d{4})/$', blog.views.ArticleListView.as_view(), name='article-list-by-year'),
    url(r'^$', blog.views.ArticleListView.as_view(), name='article-list-main-page'),
)
