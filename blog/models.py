from django.db import models
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, default='')

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = MarkdownField()
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
