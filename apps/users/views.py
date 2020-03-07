import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse

from Chuan.settings import MEDIA_KEY_PREFIX
from merchant.models import Goods
from orders.models import Cart, Order
from orders.views_constant import ORDER_STATUS_NOT_PAY, ORDER_STATUS_NOT_SEND, ORDER_STATUS_NOT_RECEIVE
from orders.views_helper import get_cart_num
from users.models import Users, Address
from users.views_constant import HTTP_USER_EXIST, HTTP_OK, HTTP_EMAIL_EXIST
from users.views_helper import hash_str, send_email_activate


def hello(request):
    return None


def register(request):
    if request.method == "GET":
        data = {
            'title': '注册'
        }
        return render(request, 'user/register.html', context=data)
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # password = hash_str(password)
        password = make_password(password)

        user = Users()
        user.u_username = username
        user.u_password = password
        user.u_email = email

        user.save()
        u_token = uuid.uuid4().hex
        cache.set(u_token, user.id, timeout=60 * 60)

        send_email_activate(username, email, u_token)

        return redirect(reverse('users:login'))


def login(request):
    if request.method == "GET":
        error_message = request.session.get('error_message')
        data = {
            'title': '登录'
        }
        if error_message:
            del request.session['error_message']
            data['error_message'] = error_message
        return render(request, 'user/login.html', context=data)
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = Users.objects.filter(Q(u_username=username) | Q(u_email=username))
        if users.exists():
            user = users.first()
            if check_password(password, user.u_password):
                if user.is_active:
                    request.session['user_id'] = user.id
                    return redirect(reverse('users:mine'))
                else:
                    request.session['error_message'] = '用户未激活'
                    redirect(reverse('users:login'))
            else:
                request.session['error_message'] = '密码错误'
                return redirect(reverse('users:login'))
        request.session['error_message'] = '用户不存在'
        return redirect(reverse('users:login'))


def check_user(request):
    username = request.GET.get('username')
    users = Users.objects.filter(u_username=username)
    data = {
        'status': HTTP_OK,
        'msg': 'username can user'
    }
    if users.exists():
        data['status'] = HTTP_USER_EXIST
        data['msg'] = 'user already exist'

    return JsonResponse(data=data)


def check_email(request):
    email = request.GET.get('email')
    emailcheck = Users.objects.filter(u_email=email)
    data = {
        'status': HTTP_OK,
        'msg': 'email can user'
    }
    if emailcheck.exists():
        data['status'] = HTTP_EMAIL_EXIST
        data['msg'] = 'user already exist'

    return JsonResponse(data=data)


def mine(request):
    user_id = request.user.id
    data = {
        'title': '我的众筹',
        'is_login': False,
        'cart_num': get_cart_num(user_id)
    }
    if user_id:
        user = Users.objects.get(pk=user_id)
        data['username'] = user.u_username
        data['is_login'] = True
        data['order_not_pay'] = Order.objects.filter(o_user=user).filter(o_status=ORDER_STATUS_NOT_PAY).count()
        data['order_not_receive'] = Order.objects.filter(o_user=user).filter(
            o_status__in=[ORDER_STATUS_NOT_RECEIVE, ORDER_STATUS_NOT_SEND]).count()

    return render(request, 'user/mine.html', context=data)


def logout(request):
    request.session.flush()
    return redirect(reverse('users:mine'))


def activate(request):
    u_token = request.GET.get('u_token')
    print(u_token)
    user_id = cache.get(u_token)
    if user_id:
        cache.delete(u_token)
        user = Users.objects.get(pk=user_id)
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))
    return render(request, 'user/activate_fail.html')


def address(request):
    user_id = request.user.id
    if request.method == 'GET':
        data = {
            'title': '我的',
            'is_login': True
        }
        user = Users.objects.get(pk=user_id)
        data['username'] = user.u_username
        user_address = Address.objects.filter(a_user_id=user_id).order_by('-a_is_default')
        data['address'] = user_address
        data['cart_num'] = get_cart_num(user_id)
        return render(request, 'user/address.html', context=data)
    elif request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address_detail = request.POST.get('address')
        code = request.POST.get("code")
        if request.POST.get('default'):
            default = True
            address_sure = Address.objects.filter(a_user_id=user_id).get(a_is_default=True)
            address_sure.a_is_default = False
            address_sure.save()
        else:
            default = False
            try:
                address_sure = Address.objects.filter(a_user_id=user_id).get(a_is_default=True)
            except Address.DoesNotExist:
                default = True
        address_obj = Address()
        address_obj.a_name = name
        address_obj.a_phone = phone
        address_obj.a_address = address_detail
        address_obj.a_code = code
        address_obj.a_is_default = default
        address_obj.a_user_id = user_id
        address_obj.save()
        return redirect(reverse('users:address'))


def mine_order(request):
    user_id = request.user.id
    user = Users.objects.get(pk=user_id)
    orders = Order.objects.filter(o_user_id=user_id).order_by('-o_time')


    # data['username'] = user.u_username
    # data['is_login'] = True
    # data['order_not_pay'] = Order.objects.filter(o_user=user).filter(o_status=ORDER_STATUS_NOT_PAY).count()
    # data['order_not_receive'] = Order.objects.filter(o_user=user).filter(
    # o_status__in=[ORDER_STATUS_NOT_RECEIVE, ORDER_STATUS_NOT_SEND]).count()
    data = {
        'title': '我的订单',
        'is_login': True,
        'username': user.u_username,
        'orders': orders,
        'MEDIA_KEY_PREFIX': MEDIA_KEY_PREFIX,
        'cart_num': get_cart_num(user_id)
    }
    return render(request, 'user/mine_order.html', context=data)
