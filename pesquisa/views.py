from django.views import generic
from catalogo.models import Product


class PesquisaProdutos(generic.ListView):
	template_name = 'pesquisa/pesquisa.html'
	context_object_name = 'produtos'

	def get_queryset(self):
		return Product.objects.filter(name__icontains=self.request.GET['name'])

pesquisa = PesquisaProdutos.as_view()



