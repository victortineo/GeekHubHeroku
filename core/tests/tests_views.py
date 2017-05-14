# coding=utf-8

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

from model_mommy import mommy

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

class LoginViewTestCase(TestCase):

	def setUp(self):
		self.client = Client() 
		self.login_url = reverse('login') 
		self.user = mommy.prepare('User')
		self.user.set_password('123')
		self.user.save()

	def tearDown(self):
		self.user.delete()

	def test_login_ok(self):
		response = self.client.get(self.login_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'login.html')
	
	def test_login_error(self):
		data = {'username': self.user.username, 'password': '1234'}
		response = self.client.post(self.login_url, data)
		self.assertFormError(response, "form", None, '')