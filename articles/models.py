from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from trydjango.utils import unique_slug_generator


class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(null=True, blank=True)


def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(article_pre_save, sender=Article)
