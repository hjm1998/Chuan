from django.urls import path

from merchant import views

app_name = 'merchant'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('register/', views.register, name='register'),
    path('checkname/', views.check_merchant_name, name='check_merchant_name'),
    path('checkidCard/', views.check_id_card, name='check_id_card'),
    path('checkphone/', views.check_phone, name='check_phone'),
    path('checkemail/', views.check_email, name='check_email'),
    path('login/', views.login, name='login'),
    path('mine/', views.mine, name='mine'),
    path('logout/', views.logout, name='logout'),
    path('publish/', views.publish, name='publish'),
]