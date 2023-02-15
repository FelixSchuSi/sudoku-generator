import unittest
from qiskit import QuantumCircuit, QuantumRegister
import qiskit.quantum_info as qi
from src.candidate_operations import two_candidate_operation
from src.candidate_operations_inverse import two_candidate_operation_inverse

from test_helpers import (
    are_all_amplitudes_in_superposition,
    are_all_amplitudes_zero,
    is_amplitude_one,
)


class TestTwoCandidateOperation(unittest.TestCase):
    def setUp(self):
        self.qr = QuantumRegister(2)
        self.q0 = self.qr[0]
        self.q1 = self.qr[1]
        self.qc = QuantumCircuit(self.qr)

    def test_zero_one(self):
        two_candidate_operation(self.qc, self.q0, self.q1, [1, 2])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, one])
        assert are_all_amplitudes_zero([two, three])

    def test_zero_one_inverse(self):
        two_candidate_operation(self.qc, self.q0, self.q1, [1, 2])
        two_candidate_operation_inverse(self.qc, self.q0, self.q1, [1, 2])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)

    def test_zero_two(self):
        two_candidate_operation(self.qc, self.q0, self.q1, [1, 3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, two])
        assert are_all_amplitudes_zero([one, three])

    def test_zero_two_inverse(self):
        two_candidate_operation(self.qc, self.q0, self.q1, [1, 3])
        two_candidate_operation_inverse(self.qc, self.q0, self.q1, [1, 3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)

    def test_zero_three(self):
        two_candidate_operation(self.qc, self.q0, self.q1, [1, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, three])
        assert are_all_amplitudes_zero([one, two])

    def test_zero_three_inverse(self):
        two_candidate_operation(self.qc, self.q0, self.q1, [1, 4])
        two_candidate_operation_inverse(self.qc, self.q0, self.q1, [1, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)

    def test_one_two(self):
        two_candidate_operation(self.qc, self.q0, self.q1, [2, 3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([one, two])
        assert are_all_amplitudes_zero([zero, three])

    def test_one_two_inverse(self):
        two_candidate_operation(self.qc, self.q0, self.q1, [2, 3])
        two_candidate_operation_inverse(self.qc, self.q0, self.q1, [2, 3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)

    def test_one_three(self):
        two_candidate_operation(self.qc, self.q0, self.q1, [2, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([one, three])
        assert are_all_amplitudes_zero([zero, two])

    def test_one_three_inverse(self):
        two_candidate_operation(self.qc, self.q0, self.q1, [2, 4])
        two_candidate_operation_inverse(self.qc, self.q0, self.q1, [2, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)

    def test_two_three(self):
        two_candidate_operation(self.qc, self.q0, self.q1, [3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([two, three])
        assert are_all_amplitudes_zero([zero, one])

    def test_two_three_inverse(self):
        two_candidate_operation(self.qc, self.q0, self.q1, [3, 4])
        two_candidate_operation_inverse(self.qc, self.q0, self.q1, [3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)


if __name__ == "__main__":
    unittest.main()
