from django.test import TestCase
from ..utils import is_name_valid, normalize_name, normalize_message

class EmptyNameTestCase(TestCase):
	def test_empty_name(self):
		self.assertFalse(is_name_valid(""))
		
