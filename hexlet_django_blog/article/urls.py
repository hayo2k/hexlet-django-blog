from django.urls import path, reverse
from hexlet_django_blog.article.views import (
    IndexView,
    ArticleView,
    ArticleFormCreateView,
    ArticleFormEditView,
    ArticleFormDeleteView,)



urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="articles_update"),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name="articles_delete"),
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"),
    path("<int:id>/", ArticleView.as_view(), name="article_show"),





]