from django.shortcuts import render
from articles.models import Article


def home(request):
    object_qs = Article.objects.all()

    context = {
        "object_list": object_qs,
    }

    return render(request, "home.html", context)


def article_search(request):
    try:
        query = int(request.GET.get("q"))
    except:
        query = None
    article = None
    if query is not None:
        article = Article.objects.get(id=query)
    context = {
        "object": article,
    }
    return render(request, "search.html", context)
