"""
Model classes and methods for the blog app
"""

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from datetime import datetime
from taggit.managers import TaggableManager


@python_2_unicode_compatible
class Blog(models.Model):
    """
    A single blog that consists of multiple articles
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField("blog title", max_length=100)
    tagline = models.CharField("blog tagline", max_length=200)
    description = models.TextField("blog description")
    posts_per_page = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Article(models.Model):
    """
    A single article
    """
    blog = models.ForeignKey(Blog)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField("article title", max_length=255)
    slug = models.SlugField("article slug", unique_for_year="published_date")
    series = models.CharField("series name", max_length=255,
                              blank=True, default="")
    teaser = models.TextField("article teaser")
    content = models.TextField("article content")
    markup_type = models.CharField(max_length=10, choices=(
        ("rst", "reStructuredText"),
        ("markdown", "Markdown"),
        ("textile", "Textile"),
        ("html", "HTML"),
    ), default="rst")
    published = models.BooleanField("published?", default=False)
    allow_comments = models.BooleanField("allow comments?", default=True)
    show_comments = models.BooleanField("show comments?", default=True)
    published_date = models.DateTimeField(
        default=datetime.now,
        help_text="The date and time this article shall appear online.")
    expiration_date = models.DateTimeField(
        blank=True, null=True,
        help_text="Leave blank if the article does not expire.")
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    edited_time = models.DateTimeField(auto_now=True, editable=False)

    objects = models.Manager()
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_date"]
        get_latest_by = "published_date"

    def get_absolute_url(self):
        return reverse('article-detail',
            kwargs={
            'pk': self.id,
            'year': self.published_date.year,
            'month': self.published_date.month,
            'slug': self.slug
            })


@python_2_unicode_compatible
class Attachment(models.Model):
    """
    An uploaded file attached to an article
    """
    path = models.FileField(upload_to=lambda inst, fn:
                            'media/%s/%s/%s' % (datetime.now().year, inst.article.slug, fn))
    article = models.ForeignKey(Article)

    def __str__(self):
        return self.path


@python_2_unicode_compatible
class Microblog(models.Model):
    """
    A ticker-style widget for displaying data from a microblog service,
    such as Twitter.
    """
    enabled = models.BooleanField("enabled?", default=True)
    blog = models.ForeignKey(Blog)
    service = models.CharField("service", max_length=100,
                               default="twitter", blank=True)
    url = models.CharField("url", max_length=255, default="", blank=True)
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    poll_minutes = models.IntegerField(default=10)
    template_path = models.CharField(max_length=255)
    next_poll_time = models.DateTimeField("time to next poll",
                                          auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.service
