from django.urls import path
from .views import Article, ArticleId

urlpatterns = [
    path('', Article.as_view()),
    path('<int:id>/', ArticleId.as_view()),
]
