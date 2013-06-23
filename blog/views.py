"""
View functions for the blog app
"""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from blog.models import Article


class ArticleListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ArticleView(DetailView):
    model = Article
