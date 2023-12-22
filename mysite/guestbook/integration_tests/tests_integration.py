from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command

from ..models import GuestbookEntry

class GuestbookIntegrationTests(TestCase):
	
	def test_message_creation_and_retrieval(self):
		# Création d'un nouveau message
		response = self.client.post(reverse('guestbook:create'), {'name': 'Test User', 'message': 'Hello, world!'})
		self.assertEqual(response.status_code, 302)  # Redirection attendue après la création

		# Récupération du message créé
		messages = GuestbookEntry.objects.all()
		self.assertEqual(len(messages), 1)
		self.assertEqual(messages[0].name, 'Test User')
		self.assertEqual(messages[0].message, 'Hello, world!')

	def test_guestbook_page(self):
		# Accès à la page du guestbook
		response = self.client.get(reverse('guestbook:list'))
		self.assertEqual(response.status_code, 200)
		self.assertIn('Hello, world!', response.content.decode())

		# Vérifiez d'autres aspects de la réponse, comme le rendu correct du template