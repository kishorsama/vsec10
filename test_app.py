import unittest
from app import app

class TestModelAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_endpoint(self):
        """Test the health check endpoint as part of Algorithm 2"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_predict_endpoint(self):
        """Validate model script endpoint as part of Algorithm 2"""
        response = self.app.post('/predict', json={"input": "test-data"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.get_json()['status'])

if __name__ == '__main__':
    unittest.main()