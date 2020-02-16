from django.contrib.auth.hashers import check_password, make_password
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from merchant.models import Merchant, Project, Goods
from merchant.views_contant import HTTP_ID_CART_EXIST, HTTP_MERCHANT_EXIST, HTTP_PHONE_EXIST, HTTP_EMAIL_EXIST


def hello(request):
    return HttpResponse("hello")


def register(request):
    if request.method == "GET":
        data = {
            'title': '商家注册'
        }
        return render(request, 'merchant/register.html', context=data)
    elif request.method == "POST":
        merchantName = request.POST.get('merchantName')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        idCard = request.POST.get('idCard')
        idCard_front = request.FILES.get('idCard_front')
        idCard_back = request.FILES.get('idCard_back')
        icon = request.FILES.get('icon')

        password = make_password(password)

        merchant = Merchant()
        merchant.m_merchantName = merchantName
        merchant.m_phone = phone
        merchant.m_email = email
        merchant.m_password = password
        merchant.m_idCard = idCard
        merchant.m_idCard_front = idCard_front
        merchant.m_idCard_back = idCard_back
        merchant.m_icon = icon
        merchant.save()
        return HttpResponse('注册成功')


def check_merchant_name(request):
    name = request.GET.get('merchantName')
    merchant = Merchant.objects.filter(m_merchantName=name)
    data = {
        'status': 200,
        'msg': '商家名可用'
    }
    if merchant.exists():
        data['status'] = HTTP_MERCHANT_EXIST
        data['msg'] = '商家名已存在'
    return JsonResponse(data=data)


def check_id_card(request):
    idCart = request.GET.get('idCart')
    merchant = Merchant.objects.filter(m_idCard=idCart)
    data = {
        'status': 200,
        'msg': '身份证可用'
    }
    if merchant.exists():
        data['status'] = HTTP_ID_CART_EXIST
        data['msg'] = '身份证已存在'
    return JsonResponse(data=data)


def check_phone(request):
    phone = request.GET.get('phone')
    merchant = Merchant.objects.filter(m_phone=phone)
    data = {
        'status': 200,
        'msg': '手机号可用'
    }
    if merchant.exists():
        data['status'] = HTTP_PHONE_EXIST
        data['msg'] = '手机号已存在'
    return JsonResponse(data=data)


def check_email(request):
    email = request.GET.get('email')
    merchant = Merchant.objects.filter(m_phone=email)
    data = {
        'status': 200,
        'msg': '邮箱号可用'
    }
    if merchant.exists():
        data['status'] = HTTP_EMAIL_EXIST
        data['msg'] = '邮箱号已存在'
    return JsonResponse(data=data)


def login(request):
    if request.method == "GET":
        error_message = request.session.get('error_message')
        data = {
            'title': '商家登录'
        }
        if error_message:
            del request.session['error_message']
            data['error_message'] = error_message
        return render(request, 'merchant/login.html', context=data)
    elif request.method == "POST":
        merchantName = request.POST.get('merchantName')
        password = request.POST.get('password')
        merchants = Merchant.objects.filter(
            Q(m_phone=merchantName) | Q(m_email=merchantName) | Q(m_merchantName=merchantName))
        if merchants.exists():
            merchant = merchants.first()
            if check_password(password, merchant.m_password):
                if merchant.is_active:
                    request.session['merchant_id'] = merchant.id
                    return redirect(reverse('merchant:mine'))
                else:
                    request.session['error_message'] = 'not activate'
                    return redirect(reverse('merchant:login'))
            else:
                request.session['error_message'] = 'password error'
                return redirect(reverse('merchant:login'))
        else:
            request.session['error_message'] = 'user does not exist'
            return redirect(reverse('merchant:login'))


def mine(request):
    merchant_id = request.session.get('merchant_id')
    data = {
        'title': '我的',
        'is_login': False
    }
    if merchant_id:
        merchant = Merchant.objects.get(pk=merchant_id)
        data['merchantName'] = merchant.m_merchantName
        data['is_login'] = True

    return render(request, 'merchant/mine.html', context=data)


def logout(request):
    request.session.flush()
    return redirect(reverse('merchant:mine'))


def publish(request):
    if request.method == "GET":
        data = {
            'title': '发起众筹',
        }
        return render(request, 'merchant/publish.html', context=data)
    elif request.method == "POST":
        p_title = request.POST.get('p_title')
        p_introText = request.POST.get('p_introText')
        p_classify = request.POST.get('p_classify')
        p_introImg = request.FILES.get('p_introImg')
        p_detail = request.FILES.get('p_detail')
        p_days = request.POST.get('p_days')
        p_target = request.POST.get('p_target')
        g_title = request.POST.get('g_title')
        g_detail = request.POST.get('g_detail')
        g_price = request.POST.get('g_price')
        g_stock = request.POST.get('g_stock')
        g_postage = request.POST.get('g_postage')
        print(p_title, p_classify, p_introImg, p_introText, p_days, p_detail, p_target, g_title, g_detail, g_price,
              g_stock, g_postage)
        project = Project()
        project.p_title = p_title
        project.p_introText = p_introText
        project.p_classify = p_classify
        project.p_introImg = p_introImg
        project.p_detail = p_detail
        project.p_days = p_days
        project.p_target = p_target
        project.save()
        goods = Goods()
        goods.g_project_id = project.id
        goods.g_title = g_title
        goods.g_detail = g_detail
        goods.g_price = g_price
        goods.g_stock = g_stock
        goods.g_postage = g_postage
        goods.save()
        return HttpResponse('hehe')
