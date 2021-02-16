import unittest
from grid import Grid

class GridTest(unittest.TestCase):

    # Test move(position, player)
    def test_move(self):
        grid = Grid()
        result = grid.move(5, "X")
        expected = {1: " ", 2: " ", 3: " ",
                    4: " ", 5: "X", 6: " ",
                    7: " ", 8: " ", 9: " "}
        self.assertTrue(result)
        self.assertEqual(expected, grid.get_grid())

    # Test are_moves_left()
    # Case: only one move has been made --> True
    def test_moves_left(self):
        grid = Grid()
        grid.move(1, "O")
        result = grid.are_moves_left()
        self.assertTrue(result)

    # Test are_moves_left() a
    # Case: all moves have been made --> False
    def test_no_moves_left(self):
        grid = Grid()
        grid.move(1, "O")
        grid.move(2, "X")
        grid.move(3, "O")
        grid.move(4, "X")
        grid.move(5, "X")
        grid.move(6, "O")
        grid.move(7, "X")
        grid.move(8, "O")
        grid.move(9, "X")
        result = grid.are_moves_left()
        self.assertFalse(result)

    # Test check_win()
    # Case: Vertical win; positions 2, 5, 8
    def test_vertical_win(self):
        grid = Grid()
        grid.move(2, "X")
        grid.move(5, "X")
        grid.move(8, "X")
        result = grid.check_win()
        expected = "X"
        self.assertEqual(result, expected)

    # Test check_win()
    # Case: Horizontal win; positions 7, 8, 9
    def test_horizontal_win(self):
        grid = Grid()
        grid.move(7, "O")
        grid.move(8, "O")
        grid.move(9, "O")
        result = grid.check_win()
        expected = "O"
        self.assertEqual(result, expected)

    # Test check_win()
    # Case: Diagonal 1 - positions 1, 5, 9
    def test_diagonal_win1(self):
        grid = Grid()
        grid.move(1, "O")
        grid.move(5, "O")
        grid.move(9, "O")
        result = grid.check_win()
        expected = "O"
        self.assertEqual(result, expected)

    # Test check_win()
    # Case: Diagonal 2 - positions 3, 5, 7
    def test_diagonal_win2(self):
        grid = Grid()
        grid.move(1, "X")
        grid.move(5, "X")
        grid.move(9, "X")
        result = grid.check_win()
        expected = "X"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()