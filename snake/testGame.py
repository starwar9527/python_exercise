import game
import unittest


class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        self.game = game.Game()

    def test_reset(self):
        self.game.reset()
        self.assertEqual(len(self.game.snake), 3)
        self.assertEqual(self.game.snake[0], self.game.head)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.iteration, 0)
        self.assertNotEqual(self.game.food, None)


if __name__ == '__main__':
    unittest.main()
