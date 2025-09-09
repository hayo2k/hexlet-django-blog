from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import CommentArticleForm, ArticleCommentForm
from hexlet_django_blog.article.models import Article
from .models import ArticleComment

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            "articles": articles
        })


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(request, "articles/show.html", context={
            "article": article,
        },
                      )


class CommentArticleView(View):
    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)
        if form.is_valid():
            comment = ArticleComment(
                content=form.cleaned_data["content"],
            )
            comment.save()

    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()
        return render(
            request, "comment.html", {"form": form}
        )

class ArticleCommentFormView(View):
    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            form.save()

