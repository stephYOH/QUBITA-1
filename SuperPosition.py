import StateTransform
import numpy as np

# define vector list for state 1 and 0 so comparison can be done
VectorState0 = [0, 0, 1]
VectorState1 = [0, 0, -1]
ErrorMessage = "The Qubit is already in a superposition state"

# define functions to generate random angles
def GenerateRandomAngleTheta():
    theta = 0
    # loop to ensure that it does not return a Base State as the random angle
    while theta == 0 or theta == 180:
        theta = np.random.uniform(0.0, 180.0)
    return theta
def GenerateRandomAnglePhi():
    # this angle defines the latitude so it does not affect the base state
    return np.random.uniform(0.0, 360.0)

# function to ensure that the state passed is not already in superposition
def CheckBasisState(stateVector): 
    if stateVector == VectorState0 or stateVector == VectorState1:
        return True
    else:
        return False


def SuperPosition(stateX, stateY, stateZ):
    theta = GenerateRandomAngleTheta()
    phi = GenerateRandomAnglePhi()
    state = [stateX, stateY, stateZ]
    basisState = CheckBasisState(state)
    if basisState:
        newState = StateTransform.TransformState(theta, phi)
        return newState, theta
    else:
        return ErrorMessage

