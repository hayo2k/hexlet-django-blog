from django.db import models
from django.urls import reverse


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('article_show', args=[self.id])



class ArticleComment(models.Model):
    content = models.CharField("content", max_length=100)
