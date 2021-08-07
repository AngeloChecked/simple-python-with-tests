import unittest

from src.folder.product import myproduct

class TestProduct(unittest.TestCase):
    def test_myproduct(self):
        num = myproduct(2,5)
        self.assertEqual(num, 10)
