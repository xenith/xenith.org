"""
View functions for the blog app
"""

from django.shortcuts import get_object_or_404, render
from .models import Article

def index(request):
    """
    Front page for a blog instance
    """
    return render(request, 'blog/index.html')

def article_list(request, *args, **kwargs):
    article_list = Article.objects.filter(published=True)

    context = {
        "article_list": article_list
    }

    return render(request, 'blog/article_list.html', context)
