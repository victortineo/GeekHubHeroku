# coding=utf-8

from django.test import TestCase, Client

class IndexViewTestCase(TestCase):
	
	def setUp(self):
		self.client = Client()

	def turnDown(self):
		pass

	def test_status_code(self):
		response = self.client.get('/')
		self.assertEquals(response.status_code, 200)

	def test_template_used(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'index.html')


