import numpy as np
from StateTransform import *
import Measure
import SuperPosition
import Gates

class BlochSphere:
    # define all the points using azimuthal and polar angle on grid 
    az, pol = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
    def __init__(self, radius):
        self.r = radius
        # initiate x, y, z values for sphere plot
        self.x = radius*np.sin(self.pol)*np.cos(self.az)
        self.y = radius*np.sin(self.pol)*np.sin(self.az)
        self.z = radius*np.cos(self.pol)

    
class StateVector:
    # declare constant numpy array for origin to plot vector state later
    VECTORTAIL = np.array([0, 0, 0])
    def __init__(self, x=float, y=float, z=float): # constructor for state vector collects x, y and z
        # ensures that all values of are between -1 and 1 for easy debugging during instantiation
        assert -1 <= x <= 1, "all values must be between -1 and 1"
        assert -1 <= y <= 1, "all values must be between -1 and 1"
        assert -1 <= z <= 1, "all values must be between -1 and 1"
        # vector state has to be a 2d array
        self.vectorState = np.array([x, y, z])
        self.theta = 0
        self.phi = 0
    
    # Call Transform State Function from StateTransform module to return new state
    # take theta and pi as argument which will be passed by user
    def RotateVector(self, theta, phi):
        newState = TransformState(
                       theta,
                       phi)
        # set theta vargument alue to pass to measure later and set vector state x, y, z values from new state
        self.theta = theta
        self.vectorState = [newState[0], newState[1], newState[2]]

   # Measuring function from measure module, return collpase state and set vector State to it 
    def Measure(self):
        # pass the theta attribute as argument
        collaspeState = Measure.Measure(self.theta)
        self.vectorState = np.array([collaspeState[0], 
                                     collaspeState[1], 
                                     collaspeState[2]])
        # change theta to 0 if collapsed state is 0 or 180 if state is 1
        if self.vectorState[2] == 1:
            self.theta = 0
        elif self.vectorState[2] == -1:
            self.theta = 180

    # Super Position funtion from superposition module        
    def InitSuperposition(self):
        # check if it returned error message i.e. Already in Superpostion, to ensure string returned is not passed to vector state
        if type(SuperPosition.SuperPosition(self.vectorState[0],
            self.vectorState[1],
            self.vectorState[2])) == str:
            # return the message to be used by error message box later
            return SuperPosition.SuperPosition(
                self.vectorState[0],
                self.vectorState[1],
                self.vectorState[2])
        newState, self.theta = SuperPosition.SuperPosition(
            self.vectorState[0],
            self.vectorState[1],
            self.vectorState[2])
        self.vectorState = np.array([newState[0], newState[1], newState[2]])

    # Pauli X gate from gates module
    def PauliX(self):
        # pass vectorState x, y and z values as argument store result in state attibute
        newState = Gates.PauliX(self.vectorState[0], 
                                self.vectorState[1], 
                                self.vectorState[2])
        self.vectorState = np.array([newState[0], newState[1], newState[2]])
        # get the theta value for measure using z = cos(theta) so theta = arccos(z) of th new gate state
        self.theta = np.arccos(self.vectorState[2]) # get theta value from z
    
    # Pauli Y gate from gates module
    def PauliY(self):
        newState = Gates.PauliY(self.vectorState[0], 
                                self.vectorState[1], 
                                self.vectorState[2])
        self.vectorState = np.array([newState[0], newState[1], newState[2]])
        self.theta = np.arccos(self.vectorState[2])
    
    # Pauli Z gate from gates module
    def PauliZ(self):
        newState = Gates.PauliZ(self.vectorState[0], 
                                self.vectorState[1], 
                                self.vectorState[2])
        self.vectorState = np.array([newState[0], newState[1], newState[2]])
        self.theta = np.arccos(self.vectorState[2])

    # PhaseGate from gates module
    def PhaseGate(self):
        newState = Gates.PhaseGate(self.vectorState[0], 
                                self.vectorState[1], 
                                self.vectorState[2])
        self.vectorState = np.array([newState[0], newState[1], newState[2]])
        self.theta = np.arccos(self.vectorState[2])
    
    # TGate from gates module
    def TGate(self):
        newState = Gates.TGate(self.vectorState[0], 
                                self.vectorState[1], 
                                self.vectorState[2])
        self.vectorState = np.array([newState[0], newState[1], newState[2]])
        self.theta = np.arccos(self.vectorState[2])
    
    # HadamardGate from gates module
    def HadamardGate(self):
        newState = Gates.HadamardGate(self.vectorState[0], 
                                self.vectorState[1], 
                                self.vectorState[2])
        self.vectorState = np.array([newState[0], newState[1], newState[2]])
        self.theta = np.arccos(self.vectorState[2])


