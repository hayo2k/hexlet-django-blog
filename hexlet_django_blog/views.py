from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html', context={"who": "World",},)


def about(request):
    return render(request, 'about.html')

