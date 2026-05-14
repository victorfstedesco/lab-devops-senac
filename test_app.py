import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertIn("SISTEMA ONLINE V1.0", response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()