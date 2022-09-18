from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm


def article_detail(request, slug=None):
    article = None
    if slug is not None:
        article = get_object_or_404(Article, slug=slug)
    context = {
        "object": article
    }

    return render(request, "articles/detail.html", context)


def article_create(request):
    form = ArticleForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        article = form.save()
        context['object'] = article
        return redirect(article.get_absolute_url())
    return render(request, "articles/create.html", context)
