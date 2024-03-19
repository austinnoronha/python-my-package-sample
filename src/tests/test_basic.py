# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
from context import generate_random_number, generate_uuid, get_answer, hello_world

class TestHelloWorld(unittest.TestCase):
    """Basic test cases."""
    
    @patch('lib.helpers.generate_uuid', return_value='12345')
    @patch('lib.helpers.generate_random_number', return_value=12345)
    def test_hello_world(self, mock_generate_random_number, mock_generate_uuid):
        expected_message = "Hello, World, your request no is: 12345-12345-12345-12345-12345"
        self.assertEqual(hello_world(), expected_message)
        
class TestHelperFunctions(unittest.TestCase):
    """Basic test cases."""
    
    @patch('lib.helpers.random.randint', return_value=12345)
    def test_generate_random_number(self, mock_randint):
        result = generate_random_number()
        self.assertEqual(result, 12345)

    @patch('lib.helpers.generate_random_number', return_value=12345)
    def test_generate_uuid(self, mock_generate_random_number):
        result = generate_uuid()
        self.assertEqual(result, '12345-12345-12345-12345-12345')

    def test_get_answer(self):
        result = get_answer()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()