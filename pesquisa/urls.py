# coding=utf-8

from django.conf.urls import url
from django.core.exceptions import ImproperlyConfigured
from . import views

app_name = 'pesquisa'
urlpatterns = [
	url(r'^', views.pesquisa, name="pesquisa"),
]