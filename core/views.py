from django.shortcuts import render
from django.http import HttpResponse
from .form import ContactForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic import View, TemplateView, CreateView
from catalogo.models import Category, Product
from django.views import generic

class indexProdutos(generic.ListView):
	
	model = Product
	template_name = 'index.html'
	context_object_name = 'produtos'
	paginate_by = 3

index = indexProdutos.as_view()

def contato(request):
	success = False
	form = ContactForm(request.POST or None)
	request.session['teste'] = 'teste'
	if form.is_valid():
		form.send_mail()
		success = True
	context = {
		'form': form,
		'success': success
	}
	return render(request, 'contato.html', context)

User = get_user_model()

