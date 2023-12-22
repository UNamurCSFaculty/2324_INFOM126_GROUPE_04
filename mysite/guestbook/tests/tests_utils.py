from django.test import TestCase
from ..utils import is_name_valid #, normalize_name, normalize_message

class EmptyNameTestCase(TestCase):
	"""Tests for is_name_valid() with empty name"""
	def test_empty_name(self):
		"""is_name_valid() should return False for empty name"""
		self.assertFalse(is_name_valid(""))
