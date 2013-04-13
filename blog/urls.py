from django.conf.urls import patterns, url
from blog.views import ArticleListView

urlpatterns = patterns('blog.views',
    url(r'^$', ArticleListView.as_view(), name='article-list'),
)
