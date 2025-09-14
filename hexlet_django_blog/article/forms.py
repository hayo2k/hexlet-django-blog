from django import forms
from django.forms import ModelForm
from .models import ArticleComment, Article

class CommentArticleForm(forms.Form):
    content = forms.CharField(label="Комментарий", max_length=200)



class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content"]


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["name", "body"]