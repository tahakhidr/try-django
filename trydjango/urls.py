from django.contrib import admin
from django.urls import path
from .views import (home)
from articles.views import article_detail


urlpatterns = [
    path('', home, name="home"),
    path('articles/<int:id>/', article_detail, name="article_detail"),
    path('admin/', admin.site.urls),
]
