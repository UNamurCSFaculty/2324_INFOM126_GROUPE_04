from django.test import TestCase

# Create your tests here.

class MyTestCase(TestCase):
    def test_always_false(self):
        self.assertFalse(True)
