from src.candidate_operations_state_vector import candidate_operation_state_vector, candidate_operation_state_vector_inverse
from src.qubit_registry import CubitRegisty

def initialize_blanks(qc, qr, candidates, qubit_registry: CubitRegisty):
    for i in range(len(candidates)):
        qubit_range_of_blank = [qubit_registry.number_of_qubits * i + num for num in range(qubit_registry.number_of_qubits)]
        candidate_operation_state_vector(qc, qubit_range_of_blank, candidates[i])


def initialize_blanks_inverse(qc, qr, candidates, qubit_registry: CubitRegisty):
    for i in range(len(candidates) - 1, -1, -1):
        qubit_range_of_blank = [qubit_registry.number_of_qubits * i + num for num in range(qubit_registry.number_of_qubits)]
        candidate_operation_state_vector_inverse(qc, qubit_range_of_blank, candidates[i])


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
        qr[qubit_registry.clause_qubits[0] : qubit_registry.ancilla_qubits[1] + 1],
        mode="v-chain",
    )
    circuit.h(qr[qubit_registry.value_qubits[1]])
    circuit.x(qr[: qubit_registry.value_qubits[1] + 1])
    initialize_blanks(circuit, qr[: qubit_registry.value_qubits[1] + 1], candidates, qubit_registry)
