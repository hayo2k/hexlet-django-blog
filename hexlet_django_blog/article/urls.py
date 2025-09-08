from django.urls import path, reverse
from hexlet_django_blog.article.views import IndexView, ArticleView



urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("<int:id>/", ArticleView.as_view(), name="article_show"),


]