# coding=utf-8

from django.conf.urls import url
from django.core.exceptions import ImproperlyConfigured
from . import views

app_name = 'categoria'
urlpatterns = [
    url(r'^$', views.produtos, name="produtos"),
 	url(r'^(?P<slug>[\w_-]+)/$', views.categoria, name='categoria'),
 	url(r'^produtos/(?P<slug>[\w_-]+)/$', views.produto, name='produto'),
]
