from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.
from blog.models import Post,Tag


class EntryAdmin(MarkdownModelAdmin):
          list_display = ("title", "created")
          prepopulated_fields = {"slug": ("title",)}




admin.site.register(Post,EntryAdmin)
admin.site.register(Tag)
