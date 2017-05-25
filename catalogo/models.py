# coding=utf-8
from django.db import models
from django.urls import reverse

class Category(models.Model): #todo objeto de modelo recebe este models.Model

	name = models.CharField('Categoria', max_length=100)
	slug = models.SlugField('Identificador', max_length=100)
	
	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado', auto_now=True)

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'
		ordering = ['name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('catalogo:categoria', kwargs={'slug': self.slug})


class Product(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Identificador', max_length=100)
	
	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado', auto_now=True)
	category = models.ForeignKey('catalogo.Category', verbose_name='Categoria')
	description = models.TextField('Descrição', blank=True)
	price = models.DecimalField('Preço', decimal_places=2, max_digits=7)


	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'
		ordering = ['name']

	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('catalogo:produto', kwargs={'slug': self.slug})