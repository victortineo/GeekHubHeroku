from django.views import generic
from catalogo.models import Product, Category


class PesquisaProdutos(generic.ListView):
	template_name = 'pesquisa/pesquisa.html'
	context_object_name = 'produtos'

	def get_queryset(self):
		tipo = self.request.GET['tipo']
		if tipo == 'nome':
			nome = self.request.GET['name']
			return Product.objects.filter(name__icontains=nome)
		if tipo == 'descricao':
			descricao = self.request.GET['descricao']
			return Product.objects.filter(description__icontains=descricao)
		if tipo == 'preco':
			if self.request.GET['preco_min'] and not self.request.GET['preco_max']:
				return Product.objects.filter(price__gte=self.request.GET['preco_min'])
			if self.request.GET['preco_max'] and not self.request.GET['preco_min']:
				return Product.objects.filter(price__lte=self.request.GET['preco_max'])
			if self.request.GET['preco_max'] and self.request.GET['preco_min']:
				return Product.objects.filter(
						price__lte=self.request.GET['preco_max'], 
						price__gte=self.request.GET['preco_min']
				)

			
				preco_max = 99999999

pesquisa = PesquisaProdutos.as_view()



