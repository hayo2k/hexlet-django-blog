from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_http_methods

def index(request, tags, article_id):
    context = {'tags': tags, 'article_id': article_id}
    return render(request, 'articles/index.html', context=context)
