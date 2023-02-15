import math


class CubitRegisty:
    def __init__(self, edges, sudoku_board, candidates):
        edges_sublist_result_qubits = 2  # Weil wir mit 2 sublisten arbeiten
        self.value_qubit_count = self.__get_value_qubits(sudoku_board)
        self.value_qubits = (0, self.value_qubit_count - 1)
        self.clause_qubit_count = math.ceil(len(edges) / edges_sublist_result_qubits)
        self.clause_qubits = (
            self.value_qubits[1] + 1,
            self.value_qubits[1] + self.clause_qubit_count,
        )
        self.ancilla_qubit_count = max(
            self.clause_qubit_count - 2,
            self.value_qubit_count - 1 - 2 - self.clause_qubit_count,
        )
        self.ancilla_qubits = (
            self.clause_qubits[1] + 1,
            self.clause_qubits[1] + self.ancilla_qubit_count,
        )
        self.edges_result_qubit_count = 1
        self.edges_result_qubits = (
            self.ancilla_qubits[1] + 1,
            self.ancilla_qubits[1] + self.edges_result_qubit_count,
        )
        self.edges_sublist_result_qubit_count = edges_sublist_result_qubits
        self.edges_sublist_result_qubits = (
            self.edges_result_qubits[1] + 1,
            self.edges_result_qubits[1] + self.edges_sublist_result_qubit_count,
        )
        self.total_qubit_count = (
            self.value_qubit_count
            + self.clause_qubit_count
            + self.ancilla_qubit_count
            + self.edges_result_qubit_count
            + self.edges_sublist_result_qubit_count
        )
        self.number_of_qubits = len(bin(len(sudoku_board) - 1).replace("0b", ""))

        print(f"Länge der Sudoku-Boards: {len(sudoku_board)} x {len(sudoku_board)}")
        print(f"Qubits pro Lücke:        {self.number_of_qubits}")
        print(f"Anzahl Qubits insgesamt: {self.total_qubit_count}")
        print(f"Anzahl Value Qubits:     {self.value_qubit_count}")
        print(f"Anzahl Clause Qubits:    {self.clause_qubit_count}")
        print(f"Anzahl Hilfsqubits:      {self.ancilla_qubit_count}")
        print(f"Edges:                   {edges}")
        print(f"Candidats:               {candidates}")

    def __get_value_qubits(self, sudoku_board):
        """
        Ermittelt die Anzahl an Qubits, die benötigt werden, um die Blanks in dem
        übergebenen Sudoku in einem Quantenschaltkreis darstellen zu können.
        """
        # Ermittelt die notwendige Anzahl an Bits um eine Dezimalzahl zu speichern.
        get_bit_for_decimal = lambda n: math.ceil(math.log(n) / math.log(2))
        number_of_empty_cells = sudoku_board.flatten().tolist().count(0)
        return number_of_empty_cells * get_bit_for_decimal(len(sudoku_board))
