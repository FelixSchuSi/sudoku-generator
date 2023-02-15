import numpy as np
from src.candidate_operations import single_candidate_operation


def single_candidate_operation_inverse(qc, q0, q1, candidates):
    """
    Invertiert die Gatter, welche von der Funktion 'single_candidate_operation'
    erstellt wurden.
    Da in der Funktion 'single_candidate_operation' nur Pauli-X Gatter verwendet,
    ist die Funktion die inverse von sich selbst.
    """
    single_candidate_operation(qc, q0, q1, candidates)


def two_candidate_operation_inverse(qc, q0, q1, candidates):
    """
    Invertiert die Gatter, welche von der Funktion 'two_candidate_operation'
    erstellt wurden.
    Dies wird erreicht, indem die durch 'two_candidate_operation' erstellten
    Gatter in umgekehrter Reihenfolge angehangen werden.
    """
    product = candidates[0] * candidates[1]
    # 1 + 2
    if product == 2:
        qc.h(q1)
    # 1 + 3
    elif product == 3:
        qc.h(q0)
    # 1 + 4
    elif product == 4:
        qc.cx(q0, q1)
        qc.h(q0)
    # 2 + 3
    elif product == 6:
        qc.cx(q0, q1)
        qc.h(q0)
        qc.x(q1)
    # 2 + 4
    elif product == 8:
        qc.h(q0)
        qc.x(q1)
    # 3 + 4
    else:
        qc.h(q1)
        qc.x(q0)


def three_candidate_operation_inverse(qc, q0, q1, candidates):
    """
    Invertiert die Gatter, welche von der Funktion 'three_candidate_operation'
    erstellt wurden.
    Dies wird erreicht, indem die durch 'three_candidate_operation' erstellten
    Gatter in umgekehrter Reihenfolge angehangen werden.
    """
    theta = 2 * np.arccos(1 / np.sqrt(3))

    if all(candidate in [1, 2, 3] for candidate in candidates):
        qc.x(q0)
        qc.ch(q0, q1)
        qc.ry(-theta, q0)

    elif all(candidate in [1, 2, 4] for candidate in candidates):
        qc.ch(q1, q0)
        qc.ry(-theta, q1)

    elif all(candidate in [2, 3, 4] for candidate in candidates):
        qc.x(q1)
        qc.ch(q0, q1)
        qc.ry(-theta, q0)

    elif all(candidate in [1, 3, 4] for candidate in candidates):
        qc.ch(q0, q1)
        qc.ry(-theta, q0)


def four_candidate_operation_inverse(qc, q0, q1, candidates):
    """
    Invertiert die Gatter, welche von der Funktion 'four_candidate_operation'
    erstellt wurden.
    Dies wird erreicht, indem die durch 'four_candidate_operation' erstellten
    Gatter in umgekehrter Reihenfolge angehangen werden.
    """
    if len(candidates) == 4:
        qc.h(q1)
        qc.h(q0)
