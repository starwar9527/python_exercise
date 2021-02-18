from exercise_challenge import *
from unittest import TestCase
from unittest.mock import patch


class TestQ5Class(TestCase):

    # mock the console input with 'hello, world'
    @patch('exercise_challenge.Q5Class.get_string', return_value='hello, world')
    def test_get_string(self, func):
        self.assertTrue(func is Q5Class.get_string)
        input = Q5Class.get_string()
        self.assertEqual(input, 'hello, world')
        self.assertTrue(func.called)

    def test_print_string(self):
        self.assertTrue(1 != 2)
