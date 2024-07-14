import agent
import game
import unittest


class TestAgent(unittest.TestCase):

    def setUp(self) -> None:
        self.agent = agent.Agent()
        self.game = game.Game()

    def test_get_state(self):
        self.game.reset()
        state = self.agent.get_state(self.game)
        self.assertEqual(len(state), 11)


if __name__ == '__main__':
    unittest.main()
