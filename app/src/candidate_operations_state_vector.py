from ast import List
import math
import numpy as np
from qiskit import QuantumCircuit

def get_desired_vector(cands, num_qubits):
    '''
    Erzeugt ein Array, welches den Statevector der value_qubit-Paare darstellt.
    Ein Paar sind die Qubits die zur Darstellung einer leeren Zelle im Sudoku benötigt werden.
    In einem 4x4-Sudoku werden beispielsweise 2 Qubits pro Zahl bzw. leerer Zelle benötigt (Zahlen 0-3 bzw. 00, 01, 10, 11).
    Cands gibt die Zahlen an, die das Paar annehmen kann. (Hinweis: Cands enthällt die Sudoku-Zahlen (1, 2, 3, 4))
    Beispiel:
    cands = [3, 4]
    desired_vector = [0, 0, 1/sqrt(2), 1/sqrt(2)]
    '''
    cands.sort()
    result = [0] * 2**num_qubits
    for candidate in cands:
        # candidate  --> binär --> führende nullen ergänzen --> binär rückwarts --> dezimal (index fürs ziel array)
        candidate = candidate - 1
        binary = bin(candidate)[2:]
        binary_with_leading_zeroes = "0" * (num_qubits - len(binary)) + binary
        binary_reverse = binary_with_leading_zeroes[::-1]
        reversed_int = int(binary_reverse, 2)
        result[reversed_int] = 1 / math.sqrt(len(cands))
    return result


def get_desired_vector_gate(desired_vector, num_qubits):
    '''
    Aus dem desired_vector wird ein Gate erzeugt, welches die Qubits dem desired_vector entsprechend initialisiert.
    '''
    qc = QuantumCircuit(num_qubits)
    qc.initialize(desired_vector, [q for q in range(num_qubits)])
    qc = qc.decompose()
    for i in reversed(range(len(qc.data)-1)):
        qc.data.pop(i)
    qc = qc.decompose().decompose().decompose().decompose().decompose().decompose()
    return qc.to_gate(label="gate")

def candidate_operation_state_vector(qc: QuantumCircuit, qubit_range, candidates):
    number_of_qubits = len(qubit_range)
    desired_vector = get_desired_vector(candidates, number_of_qubits)
    qc.append(get_desired_vector_gate(desired_vector, number_of_qubits), qubit_range)

def candidate_operation_state_vector_inverse(qc: QuantumCircuit, qubit_range, candidates):
    number_of_qubits = len(qubit_range)
    desired_vector = get_desired_vector(candidates, number_of_qubits)
    qc.append(get_desired_vector_gate(desired_vector, number_of_qubits).inverse(), qubit_range)
