from django.shortcuts import render
from .models import Article


def article_detail(request, id=None):
    article = None
    if id is not None:
        article = Article.objects.get(id=id)
    context = {
        "object": article
    }

    return render(request, "articles/detail.html", context)


def article_create(request):
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.create(title=title, content=content)
        context['object'] = article
    return render(request, "articles/create.html", context)
