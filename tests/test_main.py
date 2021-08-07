import unittest
from src.main import mysum

class TestMain(unittest.TestCase):
    def test_mysum(self):
        num = mysum(1,3)
        self.assertEqual(num, 4)

if __name__ == '__main__':
    unittest.main()
