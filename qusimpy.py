
import numpy as np

class QuantumCircuitSimulator:
    def __init__(self, nq):
        # number of qubits
        self.numberOfQubits = nq

        # initialize  corresponding vector for the qubits
        self.qubitState = np.zeros(2 ** self.numberOfQubits, dtype=int)

        # set all qubit initial states to zero
        self.qubitState[0] = 1
        """ For example, we can write 2 and 3 qubit state representions as:
        [00, 01, 10, 11] ==> Two qubit state representation has 2^2=4 basis. Number of basis equals number of elements in the array.
        [000, 001, 010, 011, 100, 101, 110, 111] ==> Three qubit state representation has 2^3=8 basis.
         """

        # define methods for the class

        # define method for gate operations on the qubit state
    def applyGate(self, gate, wireNumber):

        # initialize identity matrix for identity gate. The order of gate operations are from right to left. 
        # Right most gate represents gate applied to the first qubit in the circuit.
        identityRight = np.eye( 2 ** wireNumber, dtype=int)

        gateShape = int(gate.shape[0] ** 0.5) # it will be 1 for 2x2 matrix

        identityLeft =  np.eye( 2 ** (self.numberOfQubits - wireNumber - gateShape), dtype=int )

        gate_composed = np.kron(np.kron(identityLeft, gate), identityRight)

        # Now apply composed gate to the state vector
        self.qubitState = np.matmul(gate_composed, self.qubitState)

        # define a method for the NOT gate
    def X(self, wireNumber):
        if wireNumber >= self.numberOfQubits:
            quit("Wire number starts from zero to number of qubits -1.\n"\
             + "Wire number can not be greater than or equal number of qubits!")
            
        notGate = np.array([ [0, 1], [1, 0] ])
            
        # apply the gate operation
        self.applyGate(notGate, wireNumber)




if __name__ == "__main__":
    qc1 = QuantumCircuitSimulator(2)
    vector = qc1.qubitState
    print(vector)
    qc1.X(0)
    #qc1.X(1)
    qc1.X(2)
    print(qc1.qubitState)
    stop = 0