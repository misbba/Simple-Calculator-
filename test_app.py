"""
test_app.py - Integration tests for Flask routes and application behavior.
"""

import unittest
from app import app, HISTORY

class TestAppRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        HISTORY.clear()

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Smart Calculator', response.data)

    def test_calculate_addition(self):
        response = self.client.post('/calculate', data={
            'num1': '10',
            'num2': '20',
            'operation': 'add'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'30', response.data)
        self.assertEqual(len(HISTORY), 1)
        self.assertEqual(HISTORY[0], '10 + 20 = 30')

    def test_calculate_division_by_zero(self):
        response = self.client.post('/calculate', data={
            'num1': '10',
            'num2': '0',
            'operation': 'divide'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cannot divide by zero.', response.data)

    def test_calculate_square_root(self):
        response = self.client.post('/calculate', data={
            'num1': '25',
            'operation': 'square_root'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'5', response.data)
        self.assertIn(b'\xe2\x88\x9a25 = 5', response.data)

    def test_calculate_negative_square_root(self):
        response = self.client.post('/calculate', data={
            'num1': '-25',
            'operation': 'square_root'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cannot calculate the square root of a negative number.', response.data)

    def test_calculate_percentage(self):
        response = self.client.post('/calculate', data={
            'num1': '10',
            'num2': '500',
            'operation': 'percentage'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'50', response.data)
        self.assertIn(b'10% of 500 = 50', response.data)

    def test_clear_history(self):
        HISTORY.append('10 + 20 = 30')
        self.assertEqual(len(HISTORY), 1)
        response = self.client.post('/clear-history')
        self.assertEqual(response.status_code, 302)  # Redirects to /
        self.assertEqual(len(HISTORY), 0)

    def test_json_api_calculate(self):
        response = self.client.post('/calculate', json={
            'num1': 2,
            'num2': 5,
            'operation': 'power'
        }, headers={'X-Requested-With': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertTrue(json_data['success'])
        self.assertEqual(json_data['result'], '32')
        self.assertEqual(json_data['equation'], '2 ^ 5 = 32')

if __name__ == '__main__':
    unittest.main()
