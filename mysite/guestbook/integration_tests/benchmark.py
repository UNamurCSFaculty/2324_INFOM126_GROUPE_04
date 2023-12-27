from typing import Callable

from django.test import TestCase
from .tests_integration import GuestbookIntegrationTests as GBIT

class BenchmarkIntergrationTest(TestCase):
	"""Benchmark integration tests"""

	def test_guestbook(self, benchmark: Callable):
		"""Test guestbook"""
		benchmark(GBIT.test_message_creation_and_retrieval)
		benchmark(GBIT.test_guestbook_page)