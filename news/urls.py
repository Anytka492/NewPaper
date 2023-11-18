from django.contrib import admin
from django.urls import path
from .views import Article, ArticleId

urlpatterns = [
    path('', Article.as_view()),
    path('int:pk>/', ArticleId.as_view()),
]
