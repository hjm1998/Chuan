from django.urls import path

from apps.index import views

app_name = 'index'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('indexs/', views.index, name='indexs')
]