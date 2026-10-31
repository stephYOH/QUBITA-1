import numpy as np

# @ operator is matrix multiplication in numpy
def PauliX(x, y, z):
    #define rotation matrix for x axis with 180-degrees
    ROTATION_X_180 = np.array([[1, 0, 0], 
                       [0, np.cos(np.radians(180)), -np.sin(np.radians(180))],
                       [0, np.sin(np.radians(180)), np.cos(np.radians(180))]])
    currentState = np.array([x, y, z])
    newState = ROTATION_X_180 @ currentState
    return newState

def PauliY(x, y, z):
    #define rotation matrix for y axis with 180-degrees
    ROTATION_Y_180 = np.array([[np.cos(np.radians(180)), 0, np.sin(np.radians(180))], 
                       [0, 1, 0], 
                       [-np.sin(np.radians(180)), 0, np.cos(np.radians(180))]])
    currentState = np.array([x, y, z])
    newState = ROTATION_Y_180 @ currentState
    return newState


def PauliZ(x, y, z):
    #define rotation matrix for z axis with 180-degrees
    angle = np.radians(180)
    ROTATION_Z_180 = np.array([[np.cos(angle), -np.sin(angle), 0],
                       [np.sin(angle), np.cos(angle), 0],
                       [0, 0, 1]])
    currentState = np.array([x, y, z])
    newState = ROTATION_Z_180 @ currentState
    return newState

def PhaseGate(x, y, z):
    #define rotation matrix for z axis with 90-degrees
    angle = np.radians(90)
    currentState = np.array([x, y, z])
    ROTATION_Z_90 = np.array([[np.cos(angle), -np.sin(angle), 0],
                       [np.sin(angle), np.cos(angle), 0],
                       [0, 0, 1]])
    newState = ROTATION_Z_90 @ currentState
    return newState

def TGate(x, y, z):
    #define rotation matrix for z axis with 45-degrees
    angle = np.radians(45)
    ROTATION_Z_45 = np.array([[np.cos(angle), -np.sin(angle), 0],
                       [np.sin(angle), np.cos(angle), 0],
                       [0, 0, 1]])
    currentState = np.array([x, y, z])
    newState = ROTATION_Z_45 @ currentState
    return newState

def HadamardGate(x, y, z):
    #define rotation 90-degree in y axis and 180-degree in x axis
    angleY = np.radians(90)
    angleX = np.radians(180)
    ROTATION_Y_90 = np.array([[np.cos(angleY), 0, np.sin(angleY)], 
                       [0, 1, 0], 
                       [-np.sin(angleY), 0, np.cos(angleY)]])
    ROTATION_X_180 = np.array([[1, 0, 0], 
                       [0, np.cos(angleX), -np.sin(angleX)],
                       [0, np.sin(angleX), np.cos(angleX)]])
    currentState = np.array([x, y, z])
    newState = ROTATION_Y_90 @ ROTATION_X_180 @ currentState
    return newState

# Gates Test

# function to get var name
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

# Gates test variables
PauliXTest = PauliX(0, 0, 1)
PauliYTest = PauliY(0, 0, 1)
PauliZTest = PauliZ(-1, 0, 0)
PhaseGateTest = PhaseGate(-1, 0, 0)
TGateTest = TGate(-1, 0, 0)
HadamardGateTest = HadamardGate(0, 0, 1)

"""
# All tests
AllTests = [PauliXTest, 
            PauliYTest, 
            PauliZTest, 
            PhaseGateTest, 
            TGateTest, 
            HadamardGateTest]

# Loop through all tests, display test name and display result
for i in range(0, len(AllTests)):
    print(namestr(AllTests[i], globals()), " = ", AllTests[i])

"""