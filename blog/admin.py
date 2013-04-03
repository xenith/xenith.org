"""
Register models with admin site
"""

from django.contrib import admin
from XenithOrg.blog.models import (Article, Attachment, Blog, Microblog, Tag)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "published_date", "published")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("id", "title")
    list_filter = ("published",)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Attachment)
admin.site.register(Blog)
admin.site.register(Microblog)
admin.site.register(Tag)
