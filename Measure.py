import math
import numpy as np

# return probability of 1 using math square method
def POf1(theta):
    return math.pow(np.sin(theta/2), 2)


# use numpy Binomial to calculate which state 1 or 0 and return
def ProbableState(theta):
    pOfState1 = POf1(theta)
    # binomial method takes 1 and probaility of 1 as argument and retruns 1 or 0
    state = np.random.binomial(1, pOfState1)
    return state

# Measure Function to call from State Class
def Measure(theta):
    VECTORSTATE0 = [0, 0, 1]
    VECTORSTATE1 = [0, 0, -1]
    # get collapsed state
    collapsedState = ProbableState(theta)

    # return state vector 1 or 0 based on collapsed state
    if collapsedState == 1:
        return VECTORSTATE1
    if collapsedState == 0:
        return VECTORSTATE0