from django.urls import path
from .views import Article, ArticleId

urlpatterns = [
    path('/news', Article.as_view()),
    path('news/<int:id>/', ArticleId.as_view()),
]
