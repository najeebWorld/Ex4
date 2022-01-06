import unittest

from client_python.play_game import playgame


class MyTestCase(unittest.TestCase):
    print("zero")
    game =playgame()
    print("second")
    game.start_game()
    print("third")

    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here




if __name__ == '__main__':
    unittest.main()