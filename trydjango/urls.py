from django.contrib import admin
from django.urls import path
from .views import (home, article_search)
from articles.views import (article_detail, article_create)
from accounts.views import (register)

urlpatterns = [
    path('', home, name='home'),
    path('articles/', article_search, name='article-search'),
    path('articles/create/', article_create, name='article-create'),
    path('articles/<slug:slug>/', article_detail, name='article-detail'),
    path('admin/', admin.site.urls),

    path('accounts/register/', register, name='register'),
]
