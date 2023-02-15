import math
from src.qubit_registry import CubitRegisty

# if v1 != v2 (number) then target = 1 else target = 0
def compare_vertex(qc, qr, v1, v2, target, qubit_registry: CubitRegisty):
    """
    Japaner Code
    qc.x(qr[2 * v2])
    qc.x(qr[2 * v2 + 1])
    qc.ccx(qr[2 * v1], qr[2 * v1 + 1], target)
    qc.ccx(qr[2 * v1 + 1], qr[2 * v2], target)
    qc.ccx(qr[2 * v2], qr[2 * v2 + 1], target)
    qc.ccx(qr[2 * v1], qr[2 * v2 + 1], target)
    qc.x(qr[2 * v2 + 1])
    qc.x(qr[2 * v2])
    #
    qc.x(qr[target])
    """
    
    tempArray= []
    tempAncillaQubitsArray = []

    if qubit_registry.number_of_qubits == 1:
        tempArray.append(qubit_registry.ancilla_qubits[0])
        tempAncillaQubitsArray.append(qubit_registry.ancilla_qubits[0] + 1)

    if qubit_registry.number_of_qubits == 2:
        tempArray.append(qubit_registry.ancilla_qubits[0])
        tempArray.append(qubit_registry.ancilla_qubits[0]+1)
        tempAncillaQubitsArray.append(qubit_registry.ancilla_qubits[0] + 2)
    
    if qubit_registry.number_of_qubits == 3:
        tempArray.append(qubit_registry.ancilla_qubits[0])
        tempArray.append(qubit_registry.ancilla_qubits[0]+1)
        tempArray.append(qubit_registry.ancilla_qubits[0]+2)
        tempAncillaQubitsArray.append(qubit_registry.ancilla_qubits[0] + 3)
        tempAncillaQubitsArray.append(qubit_registry.ancilla_qubits[0] + 4)

    if qubit_registry.number_of_qubits == 4:
        tempArray.append(qubit_registry.ancilla_qubits[0])
        tempArray.append(qubit_registry.ancilla_qubits[0]+1)
        tempArray.append(qubit_registry.ancilla_qubits[0]+2)
        tempArray.append(qubit_registry.ancilla_qubits[0]+3)
        tempAncillaQubitsArray.append(qubit_registry.ancilla_qubits[0] + 4)
        tempAncillaQubitsArray.append(qubit_registry.ancilla_qubits[0] + 5)


    qc.x(qr[target])
    
    for i in range(0 , qubit_registry.number_of_qubits):
        qc.ccx(qr[qubit_registry.number_of_qubits * v1 + i], qr[qubit_registry.number_of_qubits * v2 + i],tempArray[i])

    for i in range(0 , qubit_registry.number_of_qubits):
        qc.x(qr[qubit_registry.number_of_qubits * v1 + i ])
        qc.x(qr[qubit_registry.number_of_qubits * v2  + i])

    for i in range(0 , qubit_registry.number_of_qubits):
        qc.ccx(qr[qubit_registry.number_of_qubits * v1 + i], qr[qubit_registry.number_of_qubits * v2 + i],tempArray[i])  

    qc.mct(qr[tempArray[0]: tempArray[len(tempArray)-1]+1], target, tempAncillaQubitsArray[0:len(tempAncillaQubitsArray)]  ,  mode='v-chain')
  
    for i in reversed(range(0 , qubit_registry.number_of_qubits)):
        qc.ccx(qr[qubit_registry.number_of_qubits * v1 + i], qr[qubit_registry.number_of_qubits * v2 + i],tempArray[i])

    for i in reversed(range(0 , qubit_registry.number_of_qubits)):
        qc.x(qr[qubit_registry.number_of_qubits * v1 + i ])
        qc.x(qr[qubit_registry.number_of_qubits * v2  + i])
    
    for i in reversed(range(0 , qubit_registry.number_of_qubits)):
        qc.ccx(qr[qubit_registry.number_of_qubits * v1 + i], qr[qubit_registry.number_of_qubits * v2 + i],tempArray[i])   


def compare_vertex_inv(qc, qr, v1, v2, target, qubit_registry: CubitRegisty):
    """
    Japaner Code
    qc.x(qr[target])
    #
    qc.x(qr[2 * v2])
    qc.x(qr[2 * v2 + 1])
    qc.ccx(qr[2 * v1], qr[2 * v2 + 1], target)
    qc.ccx(qr[2 * v2], qr[2 * v2 + 1], target)
    qc.ccx(qr[2 * v1 + 1], qr[2 * v2], target)
    qc.ccx(qr[2 * v1], qr[2 * v1 + 1], target)
    qc.x(qr[2 * v2 + 1])
    qc.x(qr[2 * v2])
    """

    tempArray= []
    tempAncillaQubitsArray = []


    if qubit_registry.number_of_qubits == 1:
        tempArray.append(qubit_registry.ancilla_qubits[0])
        tempAncillaQubitsArray.append(qubit_registry.ancilla_qubits[0] + 1)
        
    if qubit_registry.number_of_qubits == 2:
        tempArray.append(qubit_registry.ancilla_qubits[0])
        tempArray.append(qubit_registry.ancilla_qubits[0]+1)
        tempAncillaQubitsArray.append(qubit_registry.ancilla_qubits[0] + 2)
    
    if qubit_registry.number_of_qubits == 3:
        tempArray.append(qubit_registry.ancilla_qubits[0])
        tempArray.append(qubit_registry.ancilla_qubits[0]+1)
        tempArray.append(qubit_registry.ancilla_qubits[0]+2)
        tempAncillaQubitsArray.append(qubit_registry.ancilla_qubits[0] + 3)
        tempAncillaQubitsArray.append(qubit_registry.ancilla_qubits[0] + 4)

    if qubit_registry.number_of_qubits == 4:
        tempArray.append(qubit_registry.ancilla_qubits[0])
        tempArray.append(qubit_registry.ancilla_qubits[0]+1)
        tempArray.append(qubit_registry.ancilla_qubits[0]+2)
        tempArray.append(qubit_registry.ancilla_qubits[0]+3)
        tempAncillaQubitsArray.append(qubit_registry.ancilla_qubits[0] + 4)
        tempAncillaQubitsArray.append(qubit_registry.ancilla_qubits[0] + 5)

    for i in reversed(range(0 , qubit_registry.number_of_qubits)):
        qc.ccx(qr[qubit_registry.number_of_qubits * v1 + i], qr[qubit_registry.number_of_qubits * v2 + i],tempArray[i])

    for i in reversed(range(0 , qubit_registry.number_of_qubits)):
        qc.x(qr[qubit_registry.number_of_qubits * v1 + i ])
        qc.x(qr[qubit_registry.number_of_qubits * v2  + i])

    for i in reversed(range(0 , qubit_registry.number_of_qubits)):
        qc.ccx(qr[qubit_registry.number_of_qubits * v1 + i], qr[qubit_registry.number_of_qubits * v2 + i],tempArray[i])

    qc.mct(qr[tempArray[0]: tempArray[len(tempArray)-1]+1], target, tempAncillaQubitsArray[0:len(tempAncillaQubitsArray)]  ,  mode='v-chain')

    for i in range(0 , qubit_registry.number_of_qubits):
        qc.ccx(qr[qubit_registry.number_of_qubits * v1 + i], qr[qubit_registry.number_of_qubits * v2 + i],tempArray[i])

    for i in range(0 , qubit_registry.number_of_qubits):
        qc.x(qr[qubit_registry.number_of_qubits * v1 + i ])
        qc.x(qr[qubit_registry.number_of_qubits * v2  + i])

    for i in range(0 , qubit_registry.number_of_qubits):
        qc.ccx(qr[qubit_registry.number_of_qubits * v1 + i], qr[qubit_registry.number_of_qubits * v2 + i],tempArray[i])

    qc.x(qr[target])


def simple_oracle(qc, qr, edges, qubit_registry: CubitRegisty):
    """
    Erstellt das Orakel.

    lst1 und lst2 sind die Kanten des Graphes.
    Im Graph sind die leeren Sudoku-Felder Knoten und die Kanten beschreiben
    die Zusammenhänge zwischen Sudoku-Felder (in gleicher Spalte/Zeile/Quadrant)

    Visualisierung der Kanten siehe /kanten.png
    """
    sublists = []
    edges_per_sublist = math.ceil(len(edges)/qubit_registry.edges_sublist_result_qubit_count)
    for i in range(0,len(edges),edges_per_sublist):
        sublists.append(edges[i:i+edges_per_sublist])

    target = qubit_registry.clause_qubits[0]
    sublist_result_qubits = list(range(qubit_registry.edges_sublist_result_qubits[0], qubit_registry.edges_sublist_result_qubits[1]+1))
    def create_mct_gate(target, tmp):
        qc.mct(
            control_qubits=qr[qubit_registry.clause_qubits[0] : target],
            target_qubit=qr[tmp],
            ancilla_qubits=qr[
                qubit_registry.ancilla_qubits[0] : qubit_registry.ancilla_qubits[1] + 1
            ],
            mode="v-chain",
        )


    
    for i, sublist in enumerate(sublists):
        for elm in sublist:
            compare_vertex(qc, qr, elm[0], elm[1], target, qubit_registry)
            target += 1
        create_mct_gate(target=target, tmp=sublist_result_qubits[i])

        for elm in reversed(sublist):
            target -= 1
            compare_vertex_inv(qc, qr, elm[0], elm[1], target , qubit_registry)

    ##
    qc.mct(control_qubits=sublist_result_qubits,
           target_qubit=qr[qubit_registry.edges_result_qubits[0]]
           )
    ##

    for i, sublist in reversed(list(enumerate(sublists))):
        for elm in sublist:
            compare_vertex(qc, qr, elm[0], elm[1], target, qubit_registry)
            target += 1
        create_mct_gate(target=target, tmp=sublist_result_qubits[i])

        for elm in reversed(sublist):
            target -= 1
            compare_vertex_inv(qc, qr, elm[0], elm[1], target, qubit_registry)
