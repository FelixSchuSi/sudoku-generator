import math
import unittest
from qiskit import QuantumCircuit, QuantumRegister
import qiskit.quantum_info as qi
from src.candidate_operations_state_vector import candidate_operation_state_vector, candidate_operation_state_vector_inverse
from test_helpers import (
    are_all_amplitudes_in_superposition,
    are_all_amplitudes_zero,
    is_amplitude_one,
    is_amplitude_zero,
)

def decimal_magic(decimal_number, num_qubits):
    decimal_number = decimal_number - 1
    binary = bin(decimal_number)[2:]
    binary_with_leading_zeroes = "0" * (num_qubits - len(binary)) + binary
    binary_reverse = binary_with_leading_zeroes[::-1]
    return int(binary_reverse, 2)

class TestCandidateOperationStateVectorTwoQubit(unittest.TestCase):
    def setUp(self):
        self.qr = QuantumRegister(2)
        self.q0 = self.qr[0]
        self.q1 = self.qr[1]
        self.qc = QuantumCircuit(self.qr)

    def test_zero_one_two_three_four(self):
        candidate_operation_state_vector(self.qc, [0, 1], [1, 2, 3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, two, one, three])
    
    def test_zero_one_two(self):
        candidate_operation_state_vector(self.qc, [0,1 ], [1, 2, 3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, one, two])
        assert is_amplitude_zero(three)

    def test_zero_one_two_inverse(self):
        candidate_operation_state_vector(self.qc, [0,1 ], [1, 2, 3])
        candidate_operation_state_vector_inverse(self.qc, [0,1 ], [1, 2, 3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_zero_one_three(self):
        candidate_operation_state_vector(self.qc, [0,1 ], [1, 2, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, one, three])
        assert is_amplitude_zero(two)

    def test_zero_one_three_inverse(self):
        candidate_operation_state_vector(self.qc, [0,1 ], [1, 2, 4])
        candidate_operation_state_vector_inverse(self.qc, [0,1 ], [1, 2, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_zero_two_three(self):
        candidate_operation_state_vector(self.qc, [0,1 ], [1, 3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, two, three])
        assert is_amplitude_zero(one)

    def test_zero_two_three_inverse(self):
        candidate_operation_state_vector(self.qc, [0,1 ], [1, 3, 4])
        candidate_operation_state_vector_inverse(self.qc, [0,1 ], [1, 3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_one_two_three(self):
        candidate_operation_state_vector(self.qc, [0,1 ], [2, 3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([one, two, three])
        assert is_amplitude_zero(zero)

    def test_one_two_three_inverse(self):
        candidate_operation_state_vector(self.qc, [0,1 ], [2, 3, 4])
        candidate_operation_state_vector_inverse(self.qc, [0,1 ], [2, 3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_zero_one(self):
        candidate_operation_state_vector(self.qc, [0, 1], [1, 2])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, one])
        assert are_all_amplitudes_zero([two, three])

    def test_zero_one_inverse(self):
        candidate_operation_state_vector(self.qc, [0, 1], [1, 2])
        candidate_operation_state_vector_inverse(self.qc, [0, 1], [1, 2])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)

    def test_zero_two(self):
        candidate_operation_state_vector(self.qc, [0, 1], [1, 3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, two])
        assert are_all_amplitudes_zero([one, three])

    def test_zero_two_inverse(self):
        candidate_operation_state_vector(self.qc, [0, 1], [1, 3])
        candidate_operation_state_vector_inverse(self.qc, [0, 1], [1, 3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)

    def test_zero_three(self):
        candidate_operation_state_vector(self.qc, [0, 1], [1, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([zero, three])
        assert are_all_amplitudes_zero([one, two])

    def test_zero_three_inverse(self):
        candidate_operation_state_vector(self.qc, [0, 1], [1, 4])
        candidate_operation_state_vector_inverse(self.qc, [0, 1], [1, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)

    def test_one_two(self):
        candidate_operation_state_vector(self.qc, [0, 1], [2, 3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([one, two])
        assert are_all_amplitudes_zero([zero, three])

    def test_one_two_inverse(self):
        candidate_operation_state_vector(self.qc, [0, 1], [2, 3])
        candidate_operation_state_vector_inverse(self.qc, [0, 1], [2, 3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)

    def test_one_three(self):
        candidate_operation_state_vector(self.qc, [0, 1], [2, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([one, three])
        assert are_all_amplitudes_zero([zero, two])

    def test_one_three_inverse(self):
        candidate_operation_state_vector(self.qc, [0, 1], [2, 4])
        candidate_operation_state_vector_inverse(self.qc, [0, 1], [2, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)

    def test_two_three(self):
        candidate_operation_state_vector(self.qc, [0, 1], [3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([two, three])
        assert are_all_amplitudes_zero([zero, one])

    def test_two_three_inverse(self):
        candidate_operation_state_vector(self.qc, [0, 1], [3, 4])
        candidate_operation_state_vector_inverse(self.qc, [0, 1], [3, 4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_zero([two, one, three])
        assert is_amplitude_one(zero)

    def test_zero(self):
        candidate_operation_state_vector(self.qc, [0, 1], [1])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_zero_inverse(self):
        candidate_operation_state_vector(self.qc, [0, 1], [1])
        candidate_operation_state_vector_inverse(self.qc, [0, 1], [1])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_one(self):
        candidate_operation_state_vector(self.qc, [0, 1], [2])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(one)
        assert are_all_amplitudes_zero([zero, two, three])

    def test_one_inverse(self):
        candidate_operation_state_vector(self.qc, [0, 1], [2])
        candidate_operation_state_vector_inverse(self.qc, [0, 1], [2])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_two(self):
        candidate_operation_state_vector(self.qc, [0, 1], [3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(two)
        assert are_all_amplitudes_zero([zero, one, three])

    def test_two_inverse(self):
        candidate_operation_state_vector(self.qc, [0, 1], [3])
        candidate_operation_state_vector_inverse(self.qc, [0, 1], [3])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])

    def test_three(self):
        candidate_operation_state_vector(self.qc, [0, 1], [4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(three)
        assert are_all_amplitudes_zero([zero, one, two])

    def test_three_inverse(self):
        candidate_operation_state_vector(self.qc, [0, 1], [4])
        candidate_operation_state_vector_inverse(self.qc, [0, 1], [4])
        zero, two, one, three = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([one, two, three])


class TestCandidateOperationStateVectorThreeQubit(unittest.TestCase):
    def setUp(self):
        self.qr = QuantumRegister(3)
        self.qc = QuantumCircuit(self.qr)

    def test_zero(self):
        candidate_operation_state_vector(self.qc, [0, 1, 2], [1])
        # 000 001 010 011 100 101 110 111
        # 0    1    2   3    4    5    6    7
        # 0    4    2   6    1    5    3    7      
        zero, four, two, six, one, five, three ,seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([six, five, four, three, two, one, seven])
        candidate_operation_state_vector_inverse(self.qc, [0, 1, 2], [1])
        zero, four, two, six, one, five, three, seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([four, two, six, one, five, three, seven])

    def test_one(self):
        candidate_operation_state_vector(self.qc, [0, 1, 2], [2])   
        zero, four, two, six, one, five, three, seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(one)
        assert are_all_amplitudes_zero([zero, four, two, six, five, three ,seven])
        candidate_operation_state_vector_inverse(self.qc, [0, 1, 2], [2])
        zero, four, two, six, one, five, three, seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([four, two, six, one, five, three, seven])

    def test_two(self):
        candidate_operation_state_vector(self.qc, [0, 1, 2], [3])  
        zero, four, two, six, one, five, three ,seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(two)
        assert are_all_amplitudes_zero([zero, four, six, one, five, three ,seven])
        candidate_operation_state_vector_inverse(self.qc, [0, 1, 2], [3])
        zero, four, two, six, one, five, three, seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([four, two, six, one, five, three, seven])

    def test_three(self):
        candidate_operation_state_vector(self.qc, [0, 1, 2], [4])  
        zero, four, two, six, one, five, three ,seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(three)
        assert are_all_amplitudes_zero([zero, four, two, six, one, five, seven])
        candidate_operation_state_vector_inverse(self.qc, [0, 1, 2], [4])
        zero, four, two, six, one, five, three, seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([four, two, six, one, five, three, seven])

    def test_four(self):
        candidate_operation_state_vector(self.qc, [0, 1, 2], [5])    
        zero, four, two, six, one, five, three ,seven = qi.Statevector.from_instruction(self.qc)
        print(zero, four, two, six, one, five, three ,seven)
        assert is_amplitude_one(four)
        assert are_all_amplitudes_zero([zero, two, six, one, five, three ,seven])
        candidate_operation_state_vector_inverse(self.qc, [0, 1, 2], [5])
        zero, four, two, six, one, five, three, seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([four, two, six, one, five, three, seven])

    def test_five(self):
        candidate_operation_state_vector(self.qc, [0, 1, 2], [6])
        zero, four, two, six, one, five, three ,seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(five)
        assert are_all_amplitudes_zero([zero, four, two, six, one, three, seven])
        candidate_operation_state_vector_inverse(self.qc, [0, 1, 2], [6])
        zero, four, two, six, one, five, three, seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([four, two, six, one, five, three, seven])

    def test_six(self):
        candidate_operation_state_vector(self.qc, [0, 1, 2], [7])
        zero, four, two, six, one, five, three ,seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(six)
        assert are_all_amplitudes_zero([zero, four, two, one, five, three, seven])
        candidate_operation_state_vector_inverse(self.qc, [0, 1, 2], [7])
        zero, four, two, six, one, five, three, seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([four, two, six, one, five, three, seven])

    def test_seven(self):
        candidate_operation_state_vector(self.qc, [0, 1, 2], [8])
        zero, four, two, six, one, five, three, seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(seven)
        assert are_all_amplitudes_zero([zero, four, two, six, one, five, three])
        candidate_operation_state_vector_inverse(self.qc, [0, 1, 2], [8])
        zero, four, two, six, one, five, three, seven = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(zero)
        assert are_all_amplitudes_zero([four, two, six, one, five, three, seven])


class TestCandidateOperationStateVectorFourQubit(unittest.TestCase):
    def setUp(self):
        self.qr = QuantumRegister(4)
        self.qc = QuantumCircuit(self.qr)

    def test_in_loop(self):
        pass# TODO: Fix this dynamic test
        # for i in range(4, 17):
        #     candidate_operation_state_vector(self.qc, [0, 1, 2, 3], [i])
        #     sv = qi.Statevector.from_instruction(self.qc)
        #     magic = decimal_magic(i, 4)
        #     print("i: ", i)
        #     print("sv: ", sv)
        #     print(magic, sv[magic])
        #     print("type magic: ", type(sv[magic]), sv[magic])
        #     assert is_amplitude_one(sv[magic])
    
    def test_single_candidate(self):
        candidate_operation_state_vector(self.qc, [0, 1, 2, 3], [3])
        # 0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111
        # 0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15
        # 0    8    4    12   2    10   6    14   1    9    5    13   3    11   7    15
        zero, eight, four, twelve, two, ten, six, fourteen, one, nine, five, threeteen, three, eleven, seven, fiveteen  = qi.Statevector.from_instruction(self.qc)
        sv = qi.Statevector.from_instruction(self.qc)
        magic = decimal_magic(3, 4)
        # print("i: ", 3)
        # print("sv: ", sv)
        # print(magic, sv[magic])
        assert sv[magic] == two
        # print("type: ", type(two), two)
        assert is_amplitude_one(two)
        assert are_all_amplitudes_zero([zero, eight, four, twelve,  ten, six, fourteen, one, nine, five, threeteen, three, eleven, seven, fiveteen])

    def test_single_candidate_1(self):
        candidate_operation_state_vector(self.qc, [0, 1, 2, 3], [5])
        # 0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111
        # 0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15
        # 0    8    4    12   2    10   6    14   1    9    5    13   3    11   7    15
        zero, eight, four, twelve, two, ten, six, fourteen, one, nine, five, threeteen, three, eleven, seven, fiveteen  = qi.Statevector.from_instruction(self.qc)
        sv = qi.Statevector.from_instruction(self.qc)
        magic = decimal_magic(5, 4)
        assert sv[magic] == four
        assert is_amplitude_one(four)
        assert are_all_amplitudes_zero([zero, eight, twelve, two, ten, six, fourteen, one, nine, five, threeteen, three, eleven, seven, fiveteen])


class TestCandidateOperationStateVectorThreeQubit(unittest.TestCase):
    def setUp(self):
        self.qr = QuantumRegister(3)
        self.qc = QuantumCircuit(self.qr)
    
    def test_single_candidate(self):
        candidate_operation_state_vector(self.qc, [0, 1, 2], [3])
        # 000 001 010 011 100 101 110 111
        # 0    1    2   3   4   5   6   7
        # 0    4    2   6   1   5   3   7
        zero, four, two, six, one, five, three, seven  = qi.Statevector.from_instruction(self.qc)
        assert is_amplitude_one(two)
        assert are_all_amplitudes_zero([zero, four, six, one, five, three, seven])

    def test_two_candidates(self):
        candidate_operation_state_vector(self.qc, [0, 1, 2], [3, 4])
        # 000 001 010 011 100 101 110 111
        # 0    1    2   3   4   5   6   7
        # 0    4    2   6   1   5   3   7
        zero, four, two, six, one, five, three, seven  = qi.Statevector.from_instruction(self.qc)
        assert are_all_amplitudes_in_superposition([two, three])
        assert are_all_amplitudes_zero([zero, four, six, one, five, seven])

if __name__ == "__main__":
    unittest.main()
