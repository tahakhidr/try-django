from django.shortcuts import render
from articles.models import Article


def home(request):
    article_obj = Article.objects.get(id=2)
    object_qs = Article.objects.all()

    context = {
        "object": article_obj,
        "object_list": object_qs,
    }

    return render(request, "home.html", context)
