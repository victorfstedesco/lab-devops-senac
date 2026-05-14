import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode('utf-8'), "SISTEMA ONLINE V1.0")

if __name__ == '__main__':
    unittest.main()