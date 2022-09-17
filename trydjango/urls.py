from django.contrib import admin
from django.urls import path
from .views import (home, article_search)
from articles.views import (article_detail, article_create)
from accounts.views import (register)

urlpatterns = [
    path('', home, name='home'),
    path('articles/', article_search, name='article_search'),
    path('articles/create/', article_create, name='article_crete'),
    path('articles/<int:id>/', article_detail, name='article_detail'),
    path('admin/', admin.site.urls),

    path('accounts/register/', register, name='register'),
]
