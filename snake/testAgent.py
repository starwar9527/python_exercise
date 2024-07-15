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
        state7 = state[:7]
        exp = [0, 0, 0, 0, 1, 0, 0]
        for i in range(7):
            self.assertEqual(state7[i], exp[i])

    def test_get_move(self):
        state = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1]
        # move = self.agent.get_move(state)
        # self.assertEqual(len(move), 3)

    def test_remember(self):
        self.assertEqual(len(self.agent.memory), 0)

        state = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1]
        action = [1, 0, 0]
        reward = 10
        next_state = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]
        done = False
        self.agent.remember(state, action, reward, next_state, done)

        self.assertEqual(len(self.agent.memory), 1)
        saved = self.agent.memory[0]
        self.assertEqual(saved[0], state)
        self.assertEqual(saved[1], action)
        self.assertEqual(saved[2], reward)
        self.assertEqual(saved[3], next_state)
        self.assertEqual(saved[4], done)


if __name__ == '__main__':
    unittest.main()
