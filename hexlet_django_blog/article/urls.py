from django.shortcuts import redirect
from django.urls import path, reverse
from hexlet_django_blog.article import views


def home_redirect(request):
    return redirect(reverse('article', kwargs={'tags':'python', 'article_id': 42}))

urlpatterns = [
    path('', home_redirect),
    path('<str:tags>/<int:article_id>/', views.index, name='article'),


]