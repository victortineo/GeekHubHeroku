from django.shortcuts import render

from .models import Category, Product

def produtos(request):
	context = {
		'produtos': Product.objects.all()
	}
	return render(request, 'catalogo/produtos.html', context)


def categoria(request, slug):
	categoria = Category.objects.get(slug=slug)
	context = {
		'categoriaAtual': categoria,
		'produtos': Product.objects.filter(category=categoria),
	}
	return render(request, 'catalogo/categoria.html', context)

def produto(request, slug):
	produto = Product.objects.get(slug=slug)
	context = {
		'produto': produto,
	}
	return render(request, 'catalogo/produto.html', context)

