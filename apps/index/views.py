from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from Chuan.settings import MEDIA_KEY_PREFIX
from merchant.models import Project, Goods
from orders.models import Cart


def hello(request):
    return HttpResponse('nihao ')


def index(request):
    # page = int(request.GET.get("page", 1))
    # per_page = int(request.GET.get("per_page", 3))
    # recommend = Project.objects.all()
    # paginator = Paginator(recommend, per_page)
    # page_object = paginator.page(page)
    # data = {
    #     'page_object': page_object,
    #     'page_range': paginator.page_range
    # }
    carousel = Project.objects.order_by('?')[:5]
    recommend = Project.objects.order_by('-p_already')[0:3]
    novelty = Project.objects.filter(p_classify='科技').order_by('?')[0:4]
    data = {
        'MEDIA_KEY_PREFIX': MEDIA_KEY_PREFIX,
        'carousel': carousel,
        'recommend': recommend,
        'novelty': novelty
    }

    return render(request, 'main/index.html', context=data)


def search(request):
    data = {
        'MEDIA_KEY_PREFIX': MEDIA_KEY_PREFIX,
        'title': '查询众筹',
        'search': True,
    }
    content = request.GET.get('content')
    projects = Project.objects.filter(p_title__contains=content)
    if projects.exists():
        data['projects'] = projects
    else:
        projects = Project.objects.order_by('?')[:5]
        data['projects'] = projects
        data['search'] = False

    # 项目支持人次计算
    for project in projects:
        goods_list = Goods.objects.filter(g_project=project)
        sold = 0
        for goods in goods_list:
            sold = sold + goods.g_sold
        project.sold = sold

    return render(request, 'main/search.html', context=data)