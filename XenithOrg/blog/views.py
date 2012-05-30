"""
View functions for the blog app
"""

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext


def index(request):
    """
    Front page for a blog instance
    """
    return render_to_response('blog/index.html',
        context_instance=RequestContext(request))
