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

    def test_is_collision(self):
        self.game.reset()
        # self collision
        self.assertTrue(self.game.is_collision(self.game.snake[1]))

        # left boundary
        pt = game.Point(-10, self.game.h/2)
        self.assertTrue(self.game.is_collision(pt))

        # right boundary
        pt = game.Point(self.game.w, self.game.h/2)
        self.assertTrue(self.game.is_collision(pt))

        # down boundary
        pt = game.Point(self.game.w/2, -10)
        self.assertTrue(self.game.is_collision(pt))

        # up boundary
        pt = game.Point(self.game.w/2, self.game.h)
        self.assertTrue(self.game.is_collision(pt))

    def test_play_step(self):
        action = [1, 0, 0]
        self.game.play_step(action)
        self.assertEqual(self.game.iteration, 1)


if __name__ == '__main__':
    unittest.main()
