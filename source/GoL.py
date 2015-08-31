'''
Created on 30.08.2015

@author: Till
'''
def nextState(currentState, numberOfNeighbours):
    if currentState == Dead and numberOfNeighbours != 3:
        return Dead
    
    if numberOfNeighbours == 2 or numberOfNeighbours == 3:
        return Alive
    return Dead

class Alive():
    pass

class Dead():
    pass
