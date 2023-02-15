import unittest
from qiskit import QuantumCircuit, QuantumRegister
import qiskit.quantum_info as qi
from src.candidate_operations import single_candidate_operation
from src.candidate_operations_inverse import single_candidate_operation_inverse
from test_helpers import are_all_amplitudes_zero, is_amplitude_one


class TestSingleCandidateOperation(unittest.TestCase):
    def setUp(self):
        self.qr = QuantumRegister(2)
        self.q0 = self.qr[0]
        self.q1 = self.qr[1]
        self.qc = QuantumCircuit(self.qr)

    def test_zero(self):
        single_candidate_operation(self.qc, self.q0, self.q1, [1])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_zero_inverse(self):
        single_candidate_operation(self.qc, self.q0, self.q1, [1])
        single_candidate_operation_inverse(self.qc, self.q0, self.q1, [1])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_one(self):
        single_candidate_operation(self.qc, self.q0, self.q1, [2])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(one)
        assert are_all_amplitudes_zero([zero, two, three])

    def test_one_inverse(self):
        single_candidate_operation(self.qc, self.q0, self.q1, [2])
        single_candidate_operation_inverse(self.qc, self.q0, self.q1, [2])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_two(self):
        single_candidate_operation(self.qc, self.q0, self.q1, [3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(two)
        assert are_all_amplitudes_zero([zero, one, three])

    def test_two_inverse(self):
        single_candidate_operation(self.qc, self.q0, self.q1, [3])
        single_candidate_operation_inverse(self.qc, self.q0, self.q1, [3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_three(self):
        single_candidate_operation(self.qc, self.q0, self.q1, [4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(three)
        assert are_all_amplitudes_zero([zero, one, two])

    def test_three_inverse(self):
        single_candidate_operation(self.qc, self.q0, self.q1, [4])
        single_candidate_operation_inverse(self.qc, self.q0, self.q1, [4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])


if __name__ == "__main__":
    unittest.main()
