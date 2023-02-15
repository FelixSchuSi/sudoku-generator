import math
from numbers import Complex
from typing import List
from math import isclose
import numpy as np

equals_complex = (
    lambda a, b: isclose(a.real, b.real, abs_tol=1e-15) and isclose(a.imag, b.imag, abs_tol=1e-15)
)


def is_amplitude_zero(amplitude: Complex):
    return equals_complex(amplitude, complex(0, 0))


def are_all_amplitudes_zero(amplitudes: List[Complex]):
    return all([is_amplitude_zero(amplitude) for amplitude in amplitudes])


def is_amplitude_one(amplitude: Complex):
    return equals_complex(amplitude, complex(1, 0))


def are_all_amplitudes_one(amplitudes: List[Complex]):
    return all([is_amplitude_one(amplitude) for amplitude in amplitudes])


def are_all_amplitudes_in_superposition(amplitudes: List[Complex]):
    return all(
        [
            equals_complex(amplitude, complex(1 / np.sqrt(len(amplitudes)), 0))
            for amplitude in amplitudes
        ]
    )


def is_valid_sudoku_solution(sudoku_board):
    for rowIndex, row in enumerate(sudoku_board):
        for colIndex, cell in enumerate(row):
            for i in range(0, len(sudoku_board)):
                if (
                    sudoku_board[rowIndex][i] == sudoku_board[rowIndex][colIndex]
                    and colIndex != i
                ):
                    return False
                if (
                    sudoku_board[i][colIndex] == sudoku_board[rowIndex][colIndex]
                    and rowIndex != i
                ):
                    return False

                varRow = rowIndex % 2
                varCol = colIndex % 2
                if len(sudoku_board) == 4:
                    if varCol == 0 and varRow == 0:
                        if (
                            sudoku_board[rowIndex][colIndex]
                            == sudoku_board[rowIndex + 1][colIndex + 1]
                        ):
                            return False
                    if varCol == 0 and varRow == 1:
                        if (
                            sudoku_board[rowIndex][colIndex]
                            == sudoku_board[rowIndex - 1][colIndex + 1]
                        ):
                            return False
                    if varCol == 1 and varRow == 1:
                        if (
                            sudoku_board[rowIndex][colIndex]
                            == sudoku_board[rowIndex - 1][colIndex - 1]
                        ):
                            return False
                    if varCol == 1 and varRow == 0:
                        if (
                            sudoku_board[rowIndex][colIndex]
                            == sudoku_board[rowIndex + 1][colIndex - 1]
                        ):
                            return False
    return True
