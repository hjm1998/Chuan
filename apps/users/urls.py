from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('checkuser/', views.check_user, name='check_user'),
    path('checkemail/', views.check_email, name='check_email'),
    path('mine/', views.mine, name='mine'),
    path('logout/', views.logout, name='logout'),
    path('activate/', views.activate, name='activate'),
    path('mineorder/', views.mine_order, name='mine_order'),
    path('address/', views.address, name='address'),
    path('deleteaddr/', views.deleteaddr, name='deleteaddr'),
    path('defaultaddr/', views.defaultaddr, name='defaultaddr'),
]