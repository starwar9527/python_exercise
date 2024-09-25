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

    def win_along_dir(self):
        # check column
        self.game.set_piece(0, 1, 'X')
        self.game.set_piece(0, 2, 'X')
        self.game.set_piece(0, 3, 'X')
        self.game.set_piece(0, 4, 'X')
        self.game.set_piece(0, 5, 'X')
        self.assertTrue(self.game.win_along_dir(0, 1, 0, 1, 'X'))
        self.assertTrue(self.game.win_along_dir(0, 1, 0, 2, 'X'))
        self.assertTrue(self.game.win_along_dir(0, 1, 0, 3, 'X'))
        self.assertTrue(self.game.win_along_dir(0, 1, 0, 4, 'X'))
        self.assertTrue(self.game.win_along_dir(0, 1, 0, 5, 'X'))

        # test along rows
        self.game.reset_board()

        self.game.set_piece(1, 0, 'X')
        self.game.set_piece(2, 0, 'X')
        self.game.set_piece(3, 0, 'X')
        self.game.set_piece(4, 0, 'X')
        self.game.set_piece(5, 0, 'X')

        self.assertTrue(self.game.win_along_dir(1, 0, 1, 0, 'X'))
        self.assertTrue(self.game.win_along_dir(1, 0, 2, 0, 'X'))
        self.assertTrue(self.game.win_along_dir(1, 0, 3, 0, 'X'))
        self.assertTrue(self.game.win_along_dir(1, 0, 4, 0, 'X'))
        self.assertTrue(self.game.win_along_dir(1, 0, 5, 0, 'X'))

        # test along diagonal
        self.game.reset_board()

        self.game.set_piece(0, 0, 'X')
        self.game.set_piece(1, 1, 'X')
        self.game.set_piece(2, 2, 'X')
        self.game.set_piece(3, 3, 'X')
        self.game.set_piece(4, 4, 'X')

        self.assertTrue(self.game.win_along_dir(1, 1, 0, 0, 'X'))
        self.assertTrue(self.game.win_along_dir(1, 1, 1, 1, 'X'))
        self.assertTrue(self.game.win_along_dir(1, 1, 2, 2, 'X'))
        self.assertTrue(self.game.win_along_dir(1, 1, 3, 3, 'X'))
        self.assertTrue(self.game.win_along_dir(1, 1, 4, 4, 'X'))

        # test along the other diagonal
        self.game.reset_board()

        self.game.set_piece(0, 4, 'X')
        self.game.set_piece(1, 3, 'X')
        self.game.set_piece(2, 2, 'X')
        self.game.set_piece(3, 1, 'X')
        self.game.set_piece(4, 0, 'X')

        self.assertTrue(self.game.win_along_dir(1, -1, 0, 4, 'X'))
        self.assertTrue(self.game.win_along_dir(1, -1, 1, 3, 'X'))
        self.assertTrue(self.game.win_along_dir(1, -1, 2, 2, 'X'))
        self.assertTrue(self.game.win_along_dir(1, -1, 3, 1, 'X'))
        self.assertTrue(self.game.win_along_dir(1, -1, 4, 0, 'X'))
        
    def test_win(self):
        self.game.set_piece(0, 1, 'X')
        self.game.set_piece(0, 2, 'X')
        self.game.set_piece(0, 3, 'X')
        self.game.set_piece(0, 4, 'X')
        self.game.set_piece(0, 5, 'X')
        self.assertTrue(self.game.win(0, 5, 'X'))
        self.assertTrue(self.game.win(0, 2, 'X'))

        self.game.set_piece(0, 5, 'O')
        self.assertFalse(self.game.win(0, 1, 'X'))

    def test_reset_board(self):
        self.game.reset_board()
        for i in range(15):
            for j in range(15):
                self.assertEqual(self.game.get_piece(i, j), ' ')

        self.game.set_piece(0, 2, 'X')
        self.assertEqual(self.game.get_piece(0, 2), 'X')

        self.game.reset_board()
        self.assertEqual(self.game.get_piece(0, 2), ' ')

    def test_get_last_pos_along_dir(self):
        # test along columns
        self.game.reset_board()

        self.game.set_piece(0, 1, 'X')
        self.game.set_piece(0, 2, 'X')
        self.game.set_piece(0, 3, 'X')
        self.game.set_piece(0, 4, 'X')
        self.game.set_piece(0, 5, 'X')

        pos = self.game.get_last_pos_along_dir(0, 1, 0, 2, 'X')
        self.assertEqual(pos, 3)
        pos = self.game.get_last_pos_along_dir(0, -1, 0, 2, 'X')
        self.assertEqual(pos, 1)

        # test along rows
        self.game.reset_board()

        self.game.set_piece(1, 0, 'X')
        self.game.set_piece(2, 0, 'X')
        self.game.set_piece(3, 0, 'X')
        self.game.set_piece(4, 0, 'X')
        self.game.set_piece(5, 0, 'X')

        pos = self.game.get_last_pos_along_dir(1, 0, 2, 0, 'X')
        self.assertEqual(pos, 3)
        pos = self.game.get_last_pos_along_dir(-1, 0, 2, 0, 'X')
        self.assertEqual(pos, 1)

        # test along diagonal
        self.game.reset_board()

        self.game.set_piece(0, 0, 'X')
        self.game.set_piece(1, 1, 'X')
        self.game.set_piece(2, 2, 'X')
        self.game.set_piece(3, 3, 'X')
        self.game.set_piece(4, 4, 'X')

        pos = self.game.get_last_pos_along_dir(1, 1, 2, 2, 'X')
        self.assertEqual(pos, 2)
        pos = self.game.get_last_pos_along_dir(-1, -1, 3, 3, 'X')
        self.assertEqual(pos, 3)