import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Chuan.settings import MEDIA_KEY_PREFIX
from merchant.models import Project, Goods
from orders.models import Cart, Order, OrderGoods
from orders.views_constant import ORDER_STATUS_NOT_RECEIVE, ORDER_STATUS_NOT_PAY, ORDER_STATUS_NOT_SEND
from orders.views_helper import get_total_price, get_total_price_ordering, get_order_status, get_cart_num
from users.models import Address, AddressCopy, Users


def hello(request):
    return HttpResponse('hah')


def project(request):
    projectid = request.GET.get('projectid')
    projects = Project.objects.get(pk=projectid)
    # 计算该用户发布项目总数
    projects_count = Project.objects.filter(p_merchant_id=projects.p_merchant.id).count()
    # 日期计算
    endtime = (projects.p_time + datetime.timedelta(days=projects.p_days)).strftime("%Y-%m-%d")
    endtimeStr = datetime.datetime.strptime(endtime, "%Y-%m-%d")
    nowtime = datetime.datetime.now()
    nowtimeStr = datetime.datetime.strptime(nowtime.strftime('%Y-%m-%d'), '%Y-%m-%d')
    remaining = endtimeStr - nowtimeStr
    goods_list = Goods.objects.filter(g_project_id=projects.id)
    # 项目支持人次计算
    sold = 0
    for goods in goods_list:
        # 商品库存计算
        goods.stock = goods.g_stock - goods.g_sold
        sold = sold + goods.g_sold

    data = {
        'title': '项目',
        'projects': projects,
        'goods_list': goods_list,
        'MEDIA_KEY_PREFIX': MEDIA_KEY_PREFIX,
        'sold': sold,
        'year': endtimeStr.year,
        'month': endtimeStr.month,
        'day': endtimeStr.day,
        'remaining': remaining.days,
        'projects_count': projects_count,
    }

    user_id = request.session.get('user_id')
    if user_id:
        user = Users.objects.get(pk=user_id)
        data['username'] = user.u_username
        data['is_login'] = True
        data['cart_num'] = get_cart_num(user_id)

    return render(request, 'main/project.html', context=data)


def add_to_cart(request):
    goodsid = request.GET.get('goodsid')
    carts = Cart.objects.filter(c_user=request.user).filter(c_goods_id=goodsid)
    if carts.exists():
        cart_obj = carts.first()
        cart_obj.c_goods_num = cart_obj.c_goods_num + 1
    else:
        cart_obj = Cart()
        cart_obj.c_goods_id = goodsid
        cart_obj.c_user = request.user
    cart_obj.save()
    data = {
        'status': 200,
        'msg': 'add success',
        'c_goods_num': cart_obj.c_goods_num
    }
    return JsonResponse(data)


def cart(request):
    carts = Cart.objects.filter(c_user=request.user)
    is_all_select = not carts.filter(c_is_select=False).exists()
    is_select = carts.filter(c_is_select=True)
    all_num = 0
    for num in is_select:
        all_num = num.c_goods_num + all_num
    list_carts = {}
    for cart in carts:
        if cart.c_goods.g_project not in list_carts:
            list_carts[cart.c_goods.g_project] = []
            list_carts[cart.c_goods.g_project].append(cart)
        else:
            list_carts[cart.c_goods.g_project].append(cart)

    data = {
        'title': '购物车',
        'carts': list_carts,
        'is_all_select': is_all_select,
        'total_price': get_total_price(request.user.id),
        'MEDIA_KEY_PREFIX': MEDIA_KEY_PREFIX,
        'all_num': all_num,
        'message': '购物车'
    }

    # 查询用户名
    user_id = request.user.id
    user = Users.objects.get(pk=user_id)
    data['username'] = user.u_username
    data['is_login'] = True
    # 查询购物车数量
    data['cart_num'] = get_cart_num(user_id)

    return render(request, 'orders/cart.html', context=data)


def change_cart_state(request):
    cart_id = request.GET.get('cartid')
    cart_obj = Cart.objects.get(pk=cart_id)
    cart_obj.c_is_select = not cart_obj.c_is_select
    cart_obj.save()
    is_all_select = not Cart.objects.filter(c_user=request.user).filter(c_is_select=False).exists()

    is_select = Cart.objects.filter(c_user=request.user).filter(c_is_select=True)
    all_num = 0
    for num in is_select:
        all_num = num.c_goods_num + all_num

    data = {
        'status': 200,
        'msg': 'change ok',
        'c_is_select': cart_obj.c_is_select,
        'is_all_select': is_all_select,
        'total_price': get_total_price(request.user.id),
        'all_num': all_num,
    }

    return JsonResponse(data=data)


def sub_subshopping(request):
    cart_id = request.GET.get('cartid')
    cart_obj = Cart.objects.get(pk=cart_id)
    data = {
        'status': 200,
        'msg': 'ok',
    }
    if cart_obj.c_goods_num > 1:
        cart_obj.c_goods_num = cart_obj.c_goods_num - 1
        cart_obj.save()
        data['c_goods_num'] = cart_obj.c_goods_num
        data['price_sum'] = cart_obj.c_goods_num * cart_obj.c_goods.g_price
    # else:
    #     cart_obj.delete()
    is_select = Cart.objects.filter(c_user=request.user).filter(c_is_select=True)
    all_num = 0
    for num in is_select:
        all_num = num.c_goods_num + all_num
    data['all_num'] = all_num
    data['total_price'] = get_total_price(request.user.id)
    return JsonResponse(data=data)


def add_subshopping(request):
    cart_id = request.GET.get('cartid')
    cart_obj = Cart.objects.get(pk=cart_id)
    data = {
        'status': 200,
        'msg': 'ok'
    }
    cart_obj.c_goods_num = cart_obj.c_goods_num + 1
    cart_obj.save()
    data['c_goods_num'] = cart_obj.c_goods_num
    data['price_sum'] = cart_obj.c_goods_num * cart_obj.c_goods.g_price
    is_select = Cart.objects.filter(c_user=request.user).filter(c_is_select=True)
    all_num = 0
    for num in is_select:
        all_num = num.c_goods_num + all_num
    data['all_num'] = all_num
    data['total_price'] = get_total_price(request.user.id)
    return JsonResponse(data=data)


def all_select(request):
    cart_list = request.GET.get('cart_list')
    cart_list = cart_list.split('#')
    carts = Cart.objects.filter(id__in=cart_list)
    for cart_obj in carts:
        cart_obj.c_is_select = not cart_obj.c_is_select
        cart_obj.save()

    is_select = Cart.objects.filter(c_user=request.user).filter(c_is_select=True)
    all_num = 0
    for num in is_select:
        all_num = num.c_goods_num + all_num

    data = {
        'status': 200,
        'msg': 'ok',
        'total_price': get_total_price(request.user.id),
        'all_num': all_num,
    }
    return JsonResponse(data=data)


def ordering(request):
    user_id = request.user.id
    address = Address.objects.filter(a_user_id=user_id).order_by('-a_is_default')
    cart_obj = Cart.objects.filter(c_user_id=user_id).filter(c_is_select=True)

    list_carts = {}
    for cart in cart_obj:
        if cart.c_goods.g_project not in list_carts:
            list_carts[cart.c_goods.g_project] = []
            list_carts[cart.c_goods.g_project].append(cart)
        else:
            list_carts[cart.c_goods.g_project].append(cart)

    is_select = Cart.objects.filter(c_user=request.user).filter(c_is_select=True)
    all_num = 0
    for num in is_select:
        all_num = num.c_goods_num + all_num

    data = {
        'title': '订单结算页',
        'address': address,
        'total_price': get_total_price(user_id),
        'MEDIA_KEY_PREFIX': MEDIA_KEY_PREFIX,
        'carts': list_carts,
        'all_num': all_num
    }

    # 查询用户名
    user_id = request.user.id
    user = Users.objects.get(pk=user_id)
    data['username'] = user.u_username
    data['is_login'] = True

    return render(request, 'orders/ordering.html', context=data)


def make_order(request):
    carts = Cart.objects.filter(c_user=request.user).filter(c_is_select=True)
    temp = []
    for cart in carts:
        if cart.c_goods.g_project_id not in temp:
            temp.append(cart.c_goods.g_project.id)
            cart_objs = Cart.objects.filter(c_user=request.user).filter(
                c_goods__g_project_id=cart.c_goods.g_project_id).filter(c_is_select=True)
            order = Order()
            order.o_user = request.user
            order.o_merchant = cart.c_goods.g_project.p_merchant
            order.o_price = get_total_price_ordering(request.user.id, cart.c_goods.g_project_id)
            order.save()
            addressid = request.GET.get('addressid')
            address = Address.objects.get(pk=addressid)
            address_copy = AddressCopy()
            address_copy.a_order = order
            address_copy.a_name = address.a_name
            address_copy.a_phone = address.a_phone
            address_copy.a_address = address.a_address
            address_copy.a_code = address.a_code
            address_copy.save()
            for cart_obj in cart_objs:
                orderGoods = OrderGoods()
                orderGoods.o_order = order
                orderGoods.o_goods_num = cart_obj.c_goods_num
                orderGoods.o_goods = cart_obj.c_goods
                orderGoods.save()
                cart_obj.delete()

    data = {
        'status': 200,
        'msg': 'ok',
        'order_id': order.id
    }

    return JsonResponse(data=data)


def order_detail(request):
    order_id = request.GET.get('orderid')
    order = Order.objects.get(pk=order_id)
    address = AddressCopy.objects.get(a_order_id=order_id)
    data = {
        'title': '订单详细',
        'order': order,
        'address': address,
        'status': get_order_status(order.o_status),
        'MEDIA_KEY_PREFIX': MEDIA_KEY_PREFIX
    }

    # 查询用户名
    user_id = request.user.id
    user = Users.objects.get(pk=user_id)
    data['username'] = user.u_username
    data['is_login'] = True
    # 查询订单数量
    data['cart_num'] = get_cart_num(user_id)
    return render(request, 'orders/orderdetail.html', context=data)


def order_list_not_pay(request):
    orders = Order.objects.filter(o_user=request.user).filter(o_status=ORDER_STATUS_NOT_PAY)
    data = {
        'title': '订单列表',
        'orders': orders,
        'MEDIA_KEY_PREFIX': MEDIA_KEY_PREFIX
    }
    return render(request, 'orders/order_list_not_pay.html', context=data)


def payed(request):
    order_id = request.GET.get("orderid")
    order = Order.objects.get(pk=order_id)
    order.o_status = ORDER_STATUS_NOT_SEND
    goods = order.ordergoods_set.all().filter(o_order=order_id)

    for good in goods:
        # 项目表p_already 已筹金额更新
        project_obj = Project.objects.get(pk=good.o_goods.g_project_id)
        project_obj.p_already += good.o_goods.g_price * good.o_goods_num
        project_obj.save()
        # 商品表g_stock 库存更新
        good_obj = Goods.objects.get(pk=good.o_goods_id)
        good_obj.g_sold += 1
        good_obj.save()
    order.save()
    data = {
        'status': 200,
        'msg': 'payed success'
    }
    return JsonResponse(data=data)
