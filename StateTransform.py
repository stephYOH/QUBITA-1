import numpy as np

def TransformState(theta, phi):
    # convert to radians
    theta = np.radians(theta)
    phi = np.radians(phi)
    # create empty list for new state values and calculate x, y and z
    new_state = []
    newX = np.sin(theta) * np.cos(phi)
    newY = np.sin(theta) * np.sin(phi)
    newZ = np.cos(theta)
    # pass new value and return
    new_state = [newX, newY, newZ]

    return new_state

