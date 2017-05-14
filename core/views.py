from django.shortcuts import render
from django.http import HttpResponse
from .form import ContactForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic import View, TemplateView, CreateView

def index(request):
	return render(request, 'index.html')

def contato(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
	else:
		form = ContactForm()
	context = {
		'form': form
	}
	return render(request, 'contato.html', context)

def produto(request):
	return render(request, 'produto.html')

User = get_user_model()

