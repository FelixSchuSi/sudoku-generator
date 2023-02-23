import numpy as np
import unittest
from sudoku_grover import main
from test_helpers import is_valid_sudoku_solution


def run_test_on_sudoku_board(sudoku_board):
    print("test case: \n", sudoku_board)
    solution, _ = main(sudoku_board=sudoku_board)

    print("found solution: \n", solution)
    print("solution correct? ", is_valid_sudoku_solution(solution))
    assert is_valid_sudoku_solution(solution)


# fmt: off
class SudokuTester(unittest.TestCase):
    def test000(self):
        run_test_on_sudoku_board(
            np.array([
                [0, 0, 0, 3],
                [3, 2, 4, 0],
                [0, 4, 3, 2],
                [2, 0, 0, 0]
        ]))
    
    def test001(self):
        run_test_on_sudoku_board(
            np.array([
                [4, 0, 2, 0],
                [0, 1, 0, 4],
                [1, 0, 4, 0],
                [0, 4, 0, 2]
        ]))
    
    def test002(self):
        run_test_on_sudoku_board(
            np.array([
                [0, 0, 3, 4],
                [4, 0, 1, 2],
                [0, 1, 4, 0],
                [0, 0, 2, 0]
        ]))

    def test003(self):
        run_test_on_sudoku_board(
            np.array([
                [1, 0, 0, 0],
                [4, 3, 0, 0],
                [2, 1, 4, 0],
                [3, 4, 2, 1]
        ]))
    
    def test004(self):
        run_test_on_sudoku_board(
            np.array([
                [0, 0, 0, 0],
                [4, 3, 0, 0],
                [2, 1, 4, 0],
                [3, 4, 2, 0]
        ]))

    def test005(self):
        run_test_on_sudoku_board(
            np.array([
                [0, 0, 3, 4],
                [4, 0, 0, 2],
                [0, 1, 4, 0],
                [0, 0, 2, 0]
        ]))

    def test006(self):
        run_test_on_sudoku_board(
            np.array([
                [0, 0, 0, 0],
                [4, 3, 0, 0],
                [2, 1, 4, 0],
                [3, 4, 2, 0]
        ]))

    @unittest.skip("Sudoku momentan noch nicht lösbar - Segmentation Fault")
    def test007(self):
        run_test_on_sudoku_board(
            np.array([
                [0, 0, 0, 4],
                [4, 0, 0, 2],
                [0, 1, 4, 0],
                [0, 0, 2, 0]
        ]))

    @unittest.skip("Sudoku momentan noch nicht lösbar - läuft ewig")
    def test008(self):
        run_test_on_sudoku_board(
            np.array([
                [3, 0, 0, 0],
                [0, 0, 2, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 2]
        ]))

    def test009(self):
        run_test_on_sudoku_board(
            np.array([
                [2, 1],
                [0, 0]
        ]))

    def test010(self):
        run_test_on_sudoku_board(
            np.array([
                [9., 8., 5., 4., 2., 1., 7., 3., 6.],
                [7., 2., 4., 6., 3., 8., 5., 1., 9.],
                [1., 3., 6., 9., 5., 7., 8., 4., 2.],
                [6., 7., 3., 0., 0., 0., 1., 9., 8.],
                [4., 1., 2., 8., 7., 9., 6., 5., 3.],
                [5., 9., 8., 1., 6., 3., 4., 2., 7.],
                [3., 6., 7., 2., 1., 5., 9., 8., 4.],
                [8., 4., 1., 3., 9., 6., 2., 7., 5.],
                [2., 5., 9., 7., 8., 4., 3., 6., 1.]
        ]))

    def test011(self):
        run_test_on_sudoku_board(
            np.array([
                [1., 2., 3., 4.],
                [3., 4., 1., 2.],
                [0., 0., 0., 0.],
                [0., 0., 0., 0.]
        ]))

    def test012(self):
        run_test_on_sudoku_board(
            np.array([
                [0., 0., 5., 4., 3.],
                [0., 0., 3., 5., 4.],
                [5., 3., 4., 1., 2.],
                [4., 5., 2., 3., 1.],
                [3., 4., 1., 2., 5.]
        ]))

    def test013(self):
        run_test_on_sudoku_board(
            np.array([
                [0., 0., 0., 0.],
                [4., 3., 0., 0.],
                [2., 1., 4., 0.],
                [3., 4., 2., 0.]
        ]))

    def test014(self):
        run_test_on_sudoku_board(
            np.array([
                [0., 0., 0., 0.],
                [4., 3., 0., 0.],
                [2., 1., 4., 0.],
                [3., 4., 2., 0.]
        ]))

if __name__ == '__main__':
    unittest.main()
