# %%
from qiskit import QuantumCircuit, execute, ClassicalRegister, QuantumRegister
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from time import process_time
from qiskit_aer import AerSimulator
import numpy as np


# %%
# Alle selbst entwickelten python module sollen automatisch
# neu importiert werden, wenn sie verwendet werden.
# %load_ext autoreload
# %autoreload 2 
from src.oracle import simple_oracle
from src.diffusor import initialize_blanks, initialize_blanks_inverse
from src.request_to_sudoku_board import request_to_sudoku_board
from src.qubit_registry import CubitRegisty

# %%
def is_in_same_block(x1, y1, x2, y2, board_size):
    block_size = int(np.sqrt(board_size))
    return x1 // block_size == x2 // block_size and y1 // block_size == y2 // block_size   


# %%
import math


def get_candidates(sudoku_board):
    """
    Berechnet mögliche Werte für die Lücken im Sudoku Boad.
    Returnt eine List mit den möglichen Werten für die Lücken.

    Beispiel:
        [[3], [1, 3], [2, 3], [3], [2, 3], [3], [3]]
        In der ersten Lücke ist mit 3 zu befüllen,
        in der zweiten Lücke passen 1 und 3.
    """
    candidates = []
    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board[0])):
            if sudoku_board[i][j] != 0:
                continue
            tmp = []
            for possible_value in range(1, len(sudoku_board)+1):
                is_possible_value = True
                for row in range(len(sudoku_board)):
                    if sudoku_board[row][j] == possible_value:
                        is_possible_value = False
                for col in range(len(sudoku_board)):
                    if sudoku_board[i][col] == possible_value:
                        is_possible_value = False
                
                if math.sqrt(len(sudoku_board)).is_integer():
                    for x in range(len(sudoku_board)):
                        for y in range(len(sudoku_board)):
                            if not is_in_same_block(i, j, x, y, len(sudoku_board)):
                                continue
                            if sudoku_board[x][y] == possible_value:
                                is_possible_value = False
                if is_possible_value:
                    tmp.append(possible_value)
            candidates.append(tmp)
    return candidates



# %%
def create_edges_from_sudoku_board(sudoku_board):
    current_gap_index = 0
    existing_nodes = []
    edges = []
    for rowIndex, row in enumerate(sudoku_board):
        for colIndex, cell in enumerate(row):
            if cell != 0:
                continue
            existing_nodes.append(
                {"gap_index": current_gap_index, "y": rowIndex, "x": colIndex}
            )
            current_gap_index = current_gap_index + 1

    has_quadrants = math.sqrt(len(sudoku_board)).is_integer()

    for node in existing_nodes:
        for other_node in existing_nodes:
            if node["gap_index"] == other_node["gap_index"]:
                continue
            # Lücken in derselben Zeile finden
            if node["y"] == other_node["y"]:
                # ist diese Kante schon anders herum erfasst worden?
                if [other_node["gap_index"], node["gap_index"]] not in edges:
                    edges.append([node["gap_index"], other_node["gap_index"]])
            # Lücken in derselben Spalte finden
            if node["x"] == other_node["x"]:
                # ist diese Kante schon anders herum erfasst worden?
                if [other_node["gap_index"], node["gap_index"]] not in edges:
                    edges.append([node["gap_index"], other_node["gap_index"]])

            # Add edges for quadrants if quadrants exist
            if has_quadrants and is_in_same_block(
                node["y"], node["x"], other_node["y"], other_node["x"], len(sudoku_board)
            ):
                if [other_node["gap_index"], node["gap_index"]] not in edges and [node["gap_index"], other_node["gap_index"]] not in edges:
                    edges.append([node["gap_index"], other_node["gap_index"]])

    return edges


# %%
def diffusor(circuit, qr, candidates, qubit_registry: CubitRegisty):
    """
    diffusion (inversion about the mean) circuit.
    note that this implementation gives H^{\otimes n} (Id - |0..0><0...0|) H^{\otimes n}
    :param circuit:
    :param qr: QuantumRegister on nodes
    :return:
    """
    # Umkehrung des Anfangszustandes
    initialize_blanks_inverse(
        circuit, qr[: qubit_registry.value_qubits[1] + 1], candidates, qubit_registry
    )
    circuit.x(qr[: qubit_registry.value_qubits[1] + 1])
    # apply multi-control CZ
    circuit.h(qr[qubit_registry.value_qubits[1]])
    # circuit.mct(control_qubits=qr[:15], target_qubit=qr[15], ancilla_qubits=qr[16:29], mode='v-chain')
    circuit.mct(
        qr[: qubit_registry.value_qubits[1]],
        qr[qubit_registry.value_qubits[1]],
        qr[
            qubit_registry.clause_qubits[0] : qubit_registry.ancilla_qubits[1] + 1
        ],
        mode="basic",
    )
    circuit.h(qr[qubit_registry.value_qubits[1]])
    circuit.x(qr[: qubit_registry.value_qubits[1] + 1])
    initialize_blanks(circuit, qr[: qubit_registry.value_qubits[1] + 1], candidates, qubit_registry)


# %%
def parse_simulation_result(count, gap_count, qubit_registry: CubitRegisty) -> str:
    """
    Wandelt die Ergebnisse der Simulation in ein interpretierbares Format um.
    Return ein String, wobei jedes Zeichen des Strings den Inhalt eines freien
    Feldes vom Sudoku repräsentiert.
    """
    best_result = sorted(count.items(), key=lambda x: x[1], reverse=True)[0][0][::-1]
    result = ""
    for i in range(0, gap_count * qubit_registry.number_of_qubits, qubit_registry.number_of_qubits):
        
        tmp = "".join(best_result[i : i + qubit_registry.number_of_qubits])
        result += str(int(tmp, 2))
    return result

# %%
def fill_in_gaps(sudoku_board, solution) -> None:
    """
    Befüllt das ungelöste Sudoku Board mit der
    übergebenen Lösung
    """
    result = sudoku_board.copy()
    solutionIndex = 0
    for rowIndex, row in enumerate(sudoku_board):
        for colIndex, cell in enumerate(row):
            if sudoku_board[rowIndex][colIndex] == 0:
                result[rowIndex][colIndex] = int(solution[solutionIndex]) + 1
                solutionIndex = solutionIndex + 1
    return result


# %%
from math import prod, sqrt
from test_helpers import is_valid_sudoku_solution

def main(request_payload = None, sudoku_board = None):
    if sudoku_board is None:
        sudoku_board = request_to_sudoku_board(request_payload)
    candidates = get_candidates(sudoku_board)
    edges = create_edges_from_sudoku_board(sudoku_board=sudoku_board)
    qubit_registry = CubitRegisty(edges, sudoku_board, candidates)
    qr = QuantumRegister(qubit_registry.total_qubit_count)
    cr = ClassicalRegister(qubit_registry.value_qubit_count)
    qc = QuantumCircuit(qr, cr)
    
    initialize_blanks(qc, qr, candidates, qubit_registry)
    
    grover_iterations = max(1, int(0.5 * sqrt(prod([len(c) for c in candidates]))))
    print(f"Grover Iterationen:      {grover_iterations}")
    for i in range(grover_iterations):
        simple_oracle(qc, qr, edges, qubit_registry)
        diffusor(qc, qr, candidates, qubit_registry)

    qc.measure(
        qr[qubit_registry.value_qubits[0] : qubit_registry.value_qubits[1] + 1],
        cr[qubit_registry.value_qubits[0] : qubit_registry.value_qubits[1] + 1],
    )
    print("Simulation gestartet")
    start_time = process_time()
    job = execute(qc, backend=AerSimulator(), shots=10000)
    print(f"Simulation dauerte       {process_time() - start_time} Sekunden")
    result = job.result()

    solved_sudoku = fill_in_gaps(
        sudoku_board,
        parse_simulation_result(
            result.get_counts(),
            gap_count=sudoku_board.flatten().tolist().count(0),
            qubit_registry=qubit_registry
        ),
    )
    print("Gefundene Lösung:\n", solved_sudoku)
    print(f"Lösung korrekt?          {is_valid_sudoku_solution(solved_sudoku)}")
    return solved_sudoku, qc.qasm()


# Funktionierende Sudokus
# fmt: off
# main(request_payload={"size":4,"clues":[{"value":4,"x":0,"y":0},{"value":2,"x":2,"y":0},{"value":1,"x":1,"y":1},{"value":4,"x":3,"y":1},{"value":1,"x":0,"y":2},{"value":4,"x":2,"y":2},{"value":4,"x":1,"y":3},{"value":2,"x":3,"y":3}]})
# main(request_payload={"size": 4,"clues": [{"value": 3, "x": 3, "y": 0},{"value": 3, "x": 0, "y": 1},{"value": 2, "x": 1, "y": 1},{"value": 4, "x": 2, "y": 1},{"value": 4, "x": 1, "y": 2},{"value": 3, "x": 2, "y": 2},{"value": 2, "x": 3, "y": 2},{"value": 2, "x": 0, "y": 3}]})
# main(request_payload={"size": 4,"clues": [{"value": 1, "x": 0, "y": 0},{"value": 4, "x": 0, "y": 1},{"value": 3, "x": 1, "y": 1},{"value": 2, "x": 0, "y": 2},{"value": 1, "x": 1, "y": 2},{"value": 4, "x": 2, "y": 2},{"value": 3, "x": 0, "y": 3},{"value": 4, "x": 1, "y": 3},{"value": 2, "x": 2, "y": 3},{"value": 1, "x": 3, "y": 3},]})
# main(request_payload={"size":4,"clues":[{"value":3,"x":2,"y":0},{"value":4,"x":3,"y":0},{"value":4,"x":0,"y":1},{"value":1,"x":2,"y":1},{"value":2,"x":3,"y":1},{"value":1,"x":1,"y":2},{"value":4,"x":2,"y":2},{"value":2,"x":2,"y":3}]})
# main(request_payload={"size":4,"clues":[{"value":3,"x":2,"y":0},{"value":4,"x":3,"y":0},{"value":4,"x":0,"y":1},{"value":2,"x":3,"y":1},{"value":1,"x":1,"y":2},{"value":4,"x":2,"y":2},{"value":2,"x":2,"y":3}]})
# main(request_payload={"size":4,"clues":[{"value":4,"x":3,"y":0},{"value":4,"x":0,"y":1},{"value":2,"x":3,"y":1},{"value":1,"x":1,"y":2},{"value":4,"x":2,"y":2},{"value":3,"x":0,"y":3},{"value":2,"x":2,"y":3}]})
# main(request_payload={"size": 4,"clues": [{"value": 4, "x": 0, "y": 1},{"value": 3, "x": 1, "y": 1},{"value": 2, "x": 0, "y": 2},{"value": 1, "x": 1, "y": 2},            {"value": 4, "x": 2, "y": 2},{"value": 3, "x": 0, "y": 3},{"value": 4, "x": 1, "y": 3},{"value": 2, "x": 2, "y": 3}]})
# main(request_payload={"size":5,"clues":[{"value":5,"x":2,"y":0},{"value":4,"x":3,"y":0},{"value":3,"x":4,"y":0},{"value":3,"x":2,"y":1},{"value":5,"x":3,"y":1},{"value":4,"x":4,"y":1},{"value":5,"x":0,"y":2},{"value":3,"x":1,"y":2},{"value":4,"x":2,"y":2},{"value":1,"x":3,"y":2},{"value":2,"x":4,"y":2},{"value":4,"x":0,"y":3},{"value":5,"x":1,"y":3},{"value":2,"x":2,"y":3},{"value":3,"x":3,"y":3},{"value":1,"x":4,"y":3},{"value":3,"x":0,"y":4},{"value":4,"x":1,"y":4},{"value":1,"x":2,"y":4},{"value":2,"x":3,"y":4},{"value":5,"x":4,"y":4}]})
# main(request_payload={"size":4,"clues":[{"value":1,"x":0,"y":0},{"value":2,"x":1,"y":0},{"value":3,"x":2,"y":0},{"value":4,"x":3,"y":0},{"value":3,"x":0,"y":1},{"value":4,"x":1,"y":1},{"value":1,"x":2,"y":1},{"value":2,"x":3,"y":1}]})
# main(request_payload={"size":9,"clues":[{"value":9,"x":0,"y":0},{"value":8,"x":1,"y":0},{"value":5,"x":2,"y":0},{"value":4,"x":3,"y":0},{"value":2,"x":4,"y":0},{"value":1,"x":5,"y":0},{"value":7,"x":6,"y":0},{"value":3,"x":7,"y":0},{"value":6,"x":8,"y":0},{"value":7,"x":0,"y":1},{"value":2,"x":1,"y":1},{"value":4,"x":2,"y":1},{"value":6,"x":3,"y":1},{"value":3,"x":4,"y":1},{"value":8,"x":5,"y":1},{"value":5,"x":6,"y":1},{"value":1,"x":7,"y":1},{"value":9,"x":8,"y":1},{"value":1,"x":0,"y":2},{"value":3,"x":1,"y":2},{"value":6,"x":2,"y":2},{"value":9,"x":3,"y":2},{"value":5,"x":4,"y":2},{"value":7,"x":5,"y":2},{"value":8,"x":6,"y":2},{"value":4,"x":7,"y":2},{"value":2,"x":8,"y":2},{"value":6,"x":0,"y":3},{"value":7,"x":1,"y":3},{"value":3,"x":2,"y":3},{"value":1,"x":6,"y":3},{"value":9,"x":7,"y":3},{"value":8,"x":8,"y":3},{"value":4,"x":0,"y":4},{"value":1,"x":1,"y":4},{"value":2,"x":2,"y":4},{"value":8,"x":3,"y":4},{"value":7,"x":4,"y":4},{"value":9,"x":5,"y":4},{"value":6,"x":6,"y":4},{"value":5,"x":7,"y":4},{"value":3,"x":8,"y":4},{"value":5,"x":0,"y":5},{"value":9,"x":1,"y":5},{"value":8,"x":2,"y":5},{"value":1,"x":3,"y":5},{"value":6,"x":4,"y":5},{"value":3,"x":5,"y":5},{"value":4,"x":6,"y":5},{"value":2,"x":7,"y":5},{"value":7,"x":8,"y":5},{"value":3,"x":0,"y":6},{"value":6,"x":1,"y":6},{"value":7,"x":2,"y":6},{"value":2,"x":3,"y":6},{"value":1,"x":4,"y":6},{"value":5,"x":5,"y":6},{"value":9,"x":6,"y":6},{"value":8,"x":7,"y":6},{"value":4,"x":8,"y":6},{"value":8,"x":0,"y":7},{"value":4,"x":1,"y":7},{"value":1,"x":2,"y":7},{"value":3,"x":3,"y":7},{"value":9,"x":4,"y":7},{"value":6,"x":5,"y":7},{"value":2,"x":6,"y":7},{"value":7,"x":7,"y":7},{"value":5,"x":8,"y":7},{"value":2,"x":0,"y":8},{"value":5,"x":1,"y":8},{"value":9,"x":2,"y":8},{"value":7,"x":3,"y":8},{"value":8,"x":4,"y":8},{"value":4,"x":5,"y":8},{"value":3,"x":6,"y":8},{"value":6,"x":7,"y":8},{"value":1,"x":8,"y":8}]})
# main(request_payload={"size":2,"clues":[{"value":2,"x":0,"y":0},{"value":1,"x":1,"y":0}]})
# Noch nicht funktionierende Sudokus
# main(request_payload={"size":4,"clues":[{"value":4,"x":3,"y":0},{"value":4,"x":0,"y":1},{"value":2,"x":3,"y":1},{"value":1,"x":1,"y":2},{"value":4,"x":2,"y":2},{"value":2,"x":2,"y":3}]})

print("")


