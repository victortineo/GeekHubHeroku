# coding=utf-8

from django.conf.urls import url
from django.core.exceptions import ImproperlyConfigured
from . import views

app_name = 'compras'
urlpatterns = [
    url(r'^carrinho/adicionar/(?P<slug>[\w_-]+)/$', views.create_cart_item, name="create_cart_item"),
 	url(r'^carrinho/$', views.cart_item, name='cart_item'),
 	url(r'^finalizacao/$', views.checkout, name='checkout'),
 	url(r'^meus_pedidos/$', views.order_list, name='order_list'),		
 	url(r'^detalhes_do_pedidos/(?P<pk>\d+)/$', views.order_detail, name='order_detail'),
]
