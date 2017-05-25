"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from core import views
from catalogo import views as views_catalogo
from checkout import views as views_checkout

from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^catalogo/', include('catalogo.urls', namespace='catalogo')),
    url(r'^contato/$', views.contato, name="contato"),
    url(r'^compras/', include('checkout.urls', namespace="checkout")),
    url(r'^pesquisa/', include('pesquisa.urls', namespace="pesquisa")),
    url(r'^entrar/$', login, {'template_name':'login.html'}, name="login"),
    url(r'^sair/$', logout, {'next_page':'index'}, name="logout"),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^admin/', admin.site.urls),

]