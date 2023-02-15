import unittest
from qiskit import QuantumCircuit, QuantumRegister
import qiskit.quantum_info as qi
from src.candidate_operations import three_candidate_operation
from src.candidate_operations_inverse import three_candidate_operation_inverse
from test_helpers import (
    are_all_amplitudes_in_superposition,
    are_all_amplitudes_zero,
    is_amplitude_one,
    is_amplitude_zero,
)


class TestThreeCandidateOperation(unittest.TestCase):
    def setUp(self):
        self.qr = QuantumRegister(2)
        self.q0 = self.qr[0]
        self.q1 = self.qr[1]
        self.qc = QuantumCircuit(self.qr)

    def test_zero_one_two(self):
        three_candidate_operation(self.qc, self.q0, self.q1, [1, 2, 3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, one, two])
        assert is_amplitude_zero(three)

    def test_zero_one_two_inverse(self):
        three_candidate_operation(self.qc, self.q0, self.q1, [1, 2, 3])
        three_candidate_operation_inverse(self.qc, self.q0, self.q1, [1, 2, 3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_zero_one_three(self):
        three_candidate_operation(self.qc, self.q0, self.q1, [1, 2, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, one, three])
        assert is_amplitude_zero(two)

    def test_zero_one_three_inverse(self):
        three_candidate_operation(self.qc, self.q0, self.q1, [1, 2, 4])
        three_candidate_operation_inverse(self.qc, self.q0, self.q1, [1, 2, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_zero_two_three(self):
        three_candidate_operation(self.qc, self.q0, self.q1, [1, 3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, two, three])
        assert is_amplitude_zero(one)

    def test_zero_two_three_inverse(self):
        three_candidate_operation(self.qc, self.q0, self.q1, [1, 3, 4])
        three_candidate_operation_inverse(self.qc, self.q0, self.q1, [1, 3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_one_two_three(self):
        three_candidate_operation(self.qc, self.q0, self.q1, [2, 3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([one, two, three])
        assert is_amplitude_zero(zero)

    def test_one_two_three_inverse(self):
        three_candidate_operation(self.qc, self.q0, self.q1, [2, 3, 4])
        three_candidate_operation_inverse(self.qc, self.q0, self.q1, [2, 3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])


if __name__ == "__main__":
    unittest.main()
