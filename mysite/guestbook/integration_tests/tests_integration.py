from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command

from ..models import GuestbookEntry

class GuestbookIntegrationTests(TestCase):
	"""Tests d'intégration pour le guestbook"""
	def test_message_creation_and_retrieval(self):
		"""Teste la création et la récupération d'un message"""
		# Création d'un nouveau message
		response = self.client.post(reverse('guestbook'),
							   {'name': 'Test User', 'message': 'Hello, world!'})
		self.assertEqual(response.status_code, 302)  # Redirection attendue après la création

		# Récupération du message créé
		messages = GuestbookEntry.objects.all()
		self.assertEqual(len(messages), 1)
		self.assertEqual(messages[0].name, 'Test User')
		self.assertEqual(messages[0].message, 'Hello, world!')

	def test_guestbook_page(self):
		"""Teste l'affichage de la page du guestbook"""
		# Accès à la page du guestbook
		response = self.client.get(reverse('guestbook'))
		self.assertEqual(response.status_code, 200)
		self.assertIn('08a8d60a048c663903b52d90663df4b5', response.content.decode())

		# Vérifiez d'autres aspects de la réponse, comme le rendu correct du template
		