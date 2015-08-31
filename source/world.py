'''
Created on 31.08.2015

@author: Till
'''
from source.GoL import nextState, Alive, Dead
from source import GoL
class World():
    def __init__(self):
        self.coords = set()
    
    
    def neighbours(self, x, y):
        counter = 0
        if (x-1, y-1) in self.coords:
            counter += 1
        if (x, y-1) in self.coords:
            counter += 1
        if (x+1, y-1) in self.coords:
            counter += 1
            
        if (x-1, y) in self.coords:
            counter += 1
        if (x+1, y) in self.coords:
            counter += 1
            
        if (x-1, y+1) in self.coords:
            counter += 1
        if (x, y+1) in self.coords:
            counter += 1
        if (x+1, y+1) in self.coords:
            counter += 1
        return counter
        
    def activate(self, x, y):
        self.coords.add((x, y))
    
    def nextGeneration(self):
        newCoords = set()
        for x in range(0,501):
            for y in range(0,501):
                currentState = self.get(x, y)
                nextState = GoL.nextState(currentState, self.neighbours(x, y))
                if nextState == Alive:
                    newCoords.add((x, y))
        self.coords = newCoords
                    
            

    def get(self, x, y):
        if (x, y) in self.coords:
            return Alive
        else:
            return Dead
    