from django.conf import settings
from django.test import TestCase, LiveServerTestCase, RequestFactory
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from contact.models import Contact


class FormTests(TestCase):

	fixtures = ['blog.json']

	def setUp(self):
		self.user = User.objects.create_user('Yuki', 'pyaaron@gmail.com', '1234')

		# TODO: if User is logged in and adding form data based on that, 
		#	use the above created User to test this

	def test_contact_render(self):
		response = self.client.get(reverse('contact:contact'))
		assert response.status_code == 200

	def test_contact_form(self):
		response = self.client.post(reverse('contact:contact'), {'name': 'test',
						'email': 'pyaaron@gmail.com', 
						'subject': 'test email',
						'message': 'this is a test'}, follow=True)
		self.assertRedirects(response, '/')

	# TODO: add tests for incomplete form / wrong data i.e. bad email address
	def test_contact_empty_form(self):
		# current Contact Form objects == 0
		contacts = Contact.objects.all()
		self.assertEqual(len(contacts), 0)

		# process forms that don't work
		form_data = ['test', 'pyaaron@gmail.com', 'test email', 'this is a test']
		blank = ''
		index = 0
		for i in range(3):
			# set a blank field
			form_data = form_data
			form_data[index] = blank
			# post incomplete form
			response = self.client.post(reverse('contact:contact'), {'name': form_data[0],
							'email': form_data[1], 
							'subject': form_data[2],
							'message': form_data[3]}, follow=True)
			self.assertEqual(response.status_code, 200)
			index += 1
		# still not Contact Form objects == 0 (none created)
		contacts = Contact.objects.all()
		self.assertEqual(len(contacts), 0)












