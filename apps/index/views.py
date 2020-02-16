from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('nihao ')


def index(request):
    return render(request, 'main/index.html')