import numpy as np


def single_candidate_operation(qc, q0, q1, candidates):
    """
    Initialisiert ein Qubit Paar und schränkt die Qubits so ein,
    dass das Qubit Paar nur einen Wert annehmen kann.
    Das Qubit Paar q0 und q1 repräsentiert eine Lücke im Sudoku.

    Die Werte der Candidates beginnen bei 1, während die Werte der
    Qubits bei 0 beginnen. Dadurch entspricht ein candidate von 1
    einem Qubitwert von 0.
    """
    if candidates[0] == 1:
        pass
    elif candidates[0] == 2:
        qc.x(q1)
    elif candidates[0] == 3:
        qc.x(q0)
    else:
        qc.x(q0)
        qc.x(q1)


def two_candidate_operation(qc, q0, q1, candidates):
    """
    Initialisiert ein Qubit Paar und schränkt die Qubits so ein,
    dass das Qubit Paar ZWEI MÖGLICHE WERTE annehmen kann.
    Das Qubit Paar q0 und q1 repräsentiert eine Lücke im Sudoku.

    Die Werte der Candidates beginnen bei 1, während die Werte der
    Qubits bei 0 beginnen. Dadurch entspricht ein candidate von 1
    einem Qubitwert von 0.
    """
    product = candidates[0] * candidates[1]
    # 1 + 2
    # Erwünschte Zustände: 00, 01
    if product == 2:
        qc.h(q1)
    # 1 + 3
    # Erwünschte Zustände: 00, 10
    elif product == 3:
        qc.h(q0)
    # 1 + 4
    # Erwünschte Zustände: 00, 11
    elif product == 4:
        qc.h(q0)
        qc.cx(q0, q1)
    # 2 + 3
    # Erwünschte Zustände: 01, 10
    elif product == 6:
        qc.x(q1)
        qc.h(q0)
        qc.cx(q0, q1)
    # 2 + 4
    # Erwünschte Zustände: 01, 11
    elif product == 8:
        qc.x(q1)
        qc.h(q0)
    # 3 + 4
    # Erwünschte Zustände: 10, 11
    else:
        qc.h(q1)
        qc.x(q0)


def three_candidate_operation(qc, q0, q1, candidates):
    """
    Initialisiert ein Qubit Paar und schränkt die Qubits so ein,
    dass das Qubit Paar DREI MÖGLICHE WERTE annehmen kann.
    Das Qubit Paar q0 und q1 repräsentiert eine Lücke im Sudoku.

    Die Werte der Candidates beginnen bei 1, während die Werte der
    Qubits bei 0 beginnen. Dadurch entspricht ein candidate von 1
    einem Qubitwert von 0.
    """
    theta = 2 * np.arccos(1 / np.sqrt(3))
    # Erwünschte Zustände: 00, 01, 10
    if all(candidate in [1, 2, 3] for candidate in candidates):
        qc.ry(theta, q0)
        qc.ch(q0, q1)
        qc.x(q0)
    # Erwünschte Zustände: 00, 01, 11
    elif all(candidate in [1, 2, 4] for candidate in candidates):
        qc.ry(theta, q1)
        qc.ch(q1, q0)
    # Erwünschte Zustände: 01, 10, 11
    elif all(candidate in [2, 3, 4] for candidate in candidates):
        qc.ry(theta, q0)
        qc.ch(q0, q1)
        qc.x(q1)
    # Erwünschte Zustände: 00, 10, 11
    elif all(candidate in [1, 3, 4] for candidate in candidates):
        qc.ry(theta, q0)
        qc.ch(q0, q1)


def four_candidate_operation(qc, q0, q1, candidates):
    """
    Initialisiert ein Qubit Paar und schränkt die Qubits so ein,
    dass das Qubit Paar VIER MÖGLICHE WERTE annehmen kann.
    Das Qubit Paar q0 und q1 repräsentiert eine Lücke im Sudoku.

    Die Werte der Candidates beginnen bei 1, während die Werte der
    Qubits bei 0 beginnen. Dadurch entspricht ein candidate von 1
    einem Qubitwert von 0.
    """
    # Erwünschte Zustände: 00, 01, 10, 11
    if len(candidates) == 4:
        qc.h(q0)
        qc.h(q1)
