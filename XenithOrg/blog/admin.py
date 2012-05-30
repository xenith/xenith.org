from django.contrib import admin
from XenithOrg.blog.models import (Article, Attachment, Blog, Microblog, Tag)

admin.site.register(Article)
admin.site.register(Attachment)
admin.site.register(Blog)
admin.site.register(Microblog)
admin.site.register(Tag)
