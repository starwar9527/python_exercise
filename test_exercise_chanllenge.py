import io

from exercise_challenge import *
from unittest import TestCase
from unittest.mock import patch


class TestQ5Class(TestCase):

    # mock the console input with 'hello, world'
    @patch('builtins.input', return_value='hello, world')
    def test_get_string(self, func):
        input = Q5Class.get_string()
        self.assertEqual(input, 'hello, world')
        self.assertTrue(func.called)

    # mock the stdout print with 'HELLO, WORLD\n'
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_string(self, mock_stdout):
        Q5Class.print_string('hello, world')
        self.assertEqual(mock_stdout.getvalue(), 'HELLO, WORLD\n')
