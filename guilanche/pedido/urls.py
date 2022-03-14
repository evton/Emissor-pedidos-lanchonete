from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('novopedido/', views.novopedido, name='novopedido'),
    path('atualizapedido/<str:pk>/', views.atualizapedido, name='atualizapedido'),
    path('apagapedido/<str:pk>/', views.apagapedido, name='apagapedido'),
    path('recibo/', views.recibo, name='recibo'),
]