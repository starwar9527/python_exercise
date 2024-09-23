import unittest
import gomoku


class TestGomoku(unittest.TestCase):

    def setUp(self) -> None:
        self.game = gomoku.Gomoku()

    def test_set_piece(self):
        with self.assertRaises(ValueError):
            self.game.set_piece(-1, 0, 'w')
        with self.assertRaises(ValueError):
            self.game.set_piece(16, 1, 'w')
        with self.assertRaises(ValueError):
            self.game.set_piece(0, -1, 'w')
        with self.assertRaises(ValueError):
            self.game.set_piece(1, 16, 'w')

        self.game.set_piece(1, 1, 'w')
        self.assertEqual('w', self.game.get_piece(1, 1))

    def test_get_piece(self):
        with self.assertRaises(ValueError):
            self.game.get_piece(-1, 0)
        with self.assertRaises(ValueError):
            self.game.get_piece(16, 1)
        with self.assertRaises(ValueError):
            self.game.get_piece(0, -1)
        with self.assertRaises(ValueError):
            self.game.get_piece(1, 16)

        self.game.set_piece(2, 1, 'b')
        self.assertEqual('b', self.game.get_piece(2, 1))