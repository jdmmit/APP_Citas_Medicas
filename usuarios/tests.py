from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """Prueba básica para verificar que 1 + 1 = 2"""
        self.assertEqual(1 + 1, 2)
