import numpy as np


def request_to_sudoku_board(request_payload):
    """
    Initialisiert ein 4x4 Sudoku Board mit den übergebenen
    Vorbelegungen.
    Returnt ein zweidimensionales numpy array.
    """
    sudoku_board = np.zeros((request_payload["size"], request_payload["size"]))
    for clue in request_payload["clues"]:
        sudoku_board[clue["x"]][clue["y"]] = clue["value"]
    sudoku_board = sudoku_board.transpose()
    print("Ungelöstes Sudoku:\n", sudoku_board)
    return sudoku_board
