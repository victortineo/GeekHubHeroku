from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Category, Product

class ListaProdutos(generic.ListView):
	
	model = Product
	template_name = 'catalogo/produtos.html'
	context_object_name = 'produtos'
	paginate_by = 3

class ListaCategoria(generic.ListView):

	template_name = 'catalogo/categoria.html'
	context_object_name = 'produtos'
	paginate_by = 3

	def get_queryset(self):
		return Product.objects.filter(category__slug=self.kwargs['slug'])

	def get_context_data(self, **kwargs):
		context = super(ListaCategoria, self).get_context_data(**kwargs)
		context['categoriaAtual'] = get_object_or_404(Category, slug = self.kwargs['slug'])
		return context

def produto(request, slug):
	produto = Product.objects.get(slug=slug)
	context = {
		'produto': produto,
	}
	return render(request, 'catalogo/produto.html', context)


categoria = ListaCategoria.as_view()
produtos = ListaProdutos.as_view()