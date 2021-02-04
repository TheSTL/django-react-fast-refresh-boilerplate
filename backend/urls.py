from django.conf.urls import url
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

urlpatterns = [
    url('', index),
]
