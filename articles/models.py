from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save


class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug = slugify(self.title)
    #     super().save(args, kwargs)


def article_pre_save(instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.title)


pre_save.connect(article_pre_save, sender=Article)


def article_post_save(instance, created, *args, **kwargs):
    if created:
        print(f"{instance.title} was created")


post_save.connect(article_post_save, sender=Article)
