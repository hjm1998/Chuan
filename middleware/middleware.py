from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from merchant.models import Merchant
from users.models import Users

REQUIRE_LOGIN_JSON = [
    '/orders/addtocart/',
    '/orders/changecartstate/',
    '/orders/addshopping/',
    '/orders/subshopping/',
    '/orders/allselect/',
    '/orders/makeorder/',
]

REQUIRE_LOGIN = [
    '/orders/cart/',
    '/orders/orderdetail/',
    '/orders/orderlistnotpay/',
    '/users/address/',
    '/orders/ordering/',
    '/users/mine/',
    '/users/mineorder/',
]

REQUIRE_LOGIN_MERCHANT = [
    '/merchant/publish/',
]

class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):

        if request.path in REQUIRE_LOGIN_JSON:
            user_id = request.session.get('user_id')
            if user_id:
                try:
                    user = Users.objects.get(pk=user_id)
                    request.user = user
                except:
                    data = {
                        'status': 302,
                        'msg': 'user not avaliable'
                    }
                    return JsonResponse(data=data)
            else:
                data = {
                    'status': 302,
                    'msg': 'user not login'
                }
                return JsonResponse(data=data)

        if request.path in REQUIRE_LOGIN:
            user_id = request.session.get('user_id')
            if user_id:
                try:
                    user = Users.objects.get(pk=user_id)
                    request.user = user
                except:
                    return redirect(reverse('users:login'))
            else:
                return redirect(reverse('users:login'))

        if request.path in REQUIRE_LOGIN_MERCHANT:
            merchant_id = request.session.get('merchant_id')
            if merchant_id:
                try:
                    merchant = Merchant.objects.get(pk=merchant_id)
                    request.merchant = merchant
                except:
                    return redirect(reverse('merchant:login'))
            else:
                return redirect(reverse('merchant:login'))