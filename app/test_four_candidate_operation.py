import unittest
from qiskit import QuantumCircuit, QuantumRegister
import qiskit.quantum_info as qi
from src.candidate_operations import four_candidate_operation
from src.candidate_operations_inverse import four_candidate_operation_inverse
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

    def test_zero_one_two_three_four(self):
        four_candidate_operation(self.qc, self.q0, self.q1, [1, 2, 3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, two, one, three])

    def test_zero_one_two_three_four_inverse(self):
        four_candidate_operation(self.qc, self.q0, self.q1, [1, 2, 3, 4])
        four_candidate_operation_inverse(self.qc, self.q0, self.q1, [1, 2, 3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)


if __name__ == "__main__":
    unittest.main()
