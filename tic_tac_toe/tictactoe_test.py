import io
import unittest
from unittest.mock import patch
from tictactoe import TicTacToe

class TicTacToeTest(unittest.TestCase):
    
    # Test update_turn()
    # Case: current turn is X, update turn to O
    def test_update_turn_X(self):
        game = TicTacToe()
        game.set_turn("X")
        game.update_turn()
        result = game.get_turn()
        expected = "O"
        self.assertEqual(result, expected)

    # Test update_turn()
    # Case: current turn is O, update turn to X
    def test_update_turn_O(self):
        game = TicTacToe()
        game.set_turn("O")
        game.update_turn()
        result = game.get_turn()
        expected = "X"
        self.assertEqual(result, expected)

    # Test pick_position()
    @patch('builtins.input', side_effect=['5'])
    def test_pick_position(self, _):
        game = TicTacToe()
        result = game.pick_position()
        expected = 5
        self.assertEqual(result, expected)

    # Test play()
    # Case: Tie game
    @patch('builtins.input', side_effect=['5', '6', '3', '7', '8', '2', '1', '9', '4'])
    def test_play_and_tie(self, _):
        game = TicTacToe()
        game.play()
        result = game.get_winner()
        self.assertIsNone(result)

    # Test play()
    # Case: O Wins
    @patch('builtins.input', side_effect=['1', '5', '3', '2', '8', '6', '7', '4'])
    def test_play_and_win_O(self, _):
        game = TicTacToe()
        game.play()
        result = game.get_winner()
        expected = "O"
        self.assertEqual(result, expected)

    # Test play()
    # Case: X Wins
    @patch('builtins.input', side_effect=['5', '9', '4', '6', '3', '8', '7'])
    def test_play_and_win_X(self, _):
        game = TicTacToe()
        game.play()
        result = game.get_winner()
        expected = "X"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()