#coding=utf-8

from django.test import TestCase
from model_mommy import mommy
from django.core.urlresolvers import reverse
from catalogo.models import Category, Product

class CategoryTestCase(TestCase):

	def setUp(self):
		self.category = mommy.make('catalogo.Category')

	def test_get_absolute_url(self):
		self.assertEquals(
			self.category.get_absolute_url(),
			reverse('catalogo.Category', kwargs={'slug': self.category.slug})
		)

class CategoryTestCase(TestCase):
	
	def setUp(self):
		self.produto = mommy.make(Produto)

	def test_get_absolute_url(self):
		self.assertEquals(
			self.produto.get_absolute_url(),
			reverse('catalogo.Product', kwargs={'slug': self.produto.slug})
		)