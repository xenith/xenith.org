"""
Register models with admin site
"""

from __future__ import unicode_literals
from django.contrib import admin
from blog.models import Article, Attachment, Blog, Microblog


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "tags", "published_date", "published")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("id", "title")
    list_filter = ("published",)
    list_per_page = 25

admin.site.register(Article, ArticleAdmin)
admin.site.register(Attachment)
admin.site.register(Blog)
admin.site.register(Microblog)
