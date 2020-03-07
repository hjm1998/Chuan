from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from orders.models import Cart


def hello(request):
    return HttpResponse('nihao ')


def index(request):
    return render(request, 'main/index.html')
