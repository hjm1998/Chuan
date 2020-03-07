from django.urls import path

from orders import views

app_name = 'orders'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('project/', views.project, name='project'),
    path('addtocart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('changecartstate/', views.change_cart_state, name='change_cart_state'),
    path('subshopping/', views.sub_subshopping, name='sub_shopping'),
    path('addshopping/', views.add_subshopping, name='add_shopping'),
    path('allselect/', views.all_select, name='all_select'),
    path('ordering/', views.ordering, name='ordering'),
    path('makeorder/', views.make_order, name='make_order'),
    path('orderdetail/', views.order_detail, name='order_detail'),
    path('orderlistnotpay/', views.order_list_not_pay, name='order_list_not_pay'),
    path('payed/', views.payed, name='payed'),
]
