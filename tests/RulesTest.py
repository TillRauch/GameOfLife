'''
Created on 30.08.2015

@author: Till
'''
import unittest
from source.GoL import Alive, nextState, Dead
from sets import Set


class World():
    coords = Set() 
    
    
    def neighbours(self, x, y):
        counter = 0
        if [x-1, y-1] in self.coords:
            counter += 1
        if [x, y-1] in self.coords:
            counter += 1
        if [x+1, y-1] in self.coords:
            counter += 1
            
        if [x-1, y] in self.coords:
            counter += 1
        if [x+1, y] in self.coords:
            counter += 1
            
        if [x-1, y+1] in self.coords:
            counter += 1
        if [x, y+1] in self.coords:
            counter += 1
        if [x+1, y+1] in self.coords:
            counter += 1
        return counter
        
    def activate(self, x, y):
        self.coords.append([x, y])
    
    def nextGeneration(self):
        for x in range(0,501):
            for y in range(0,501):
                currentState = World.get(self, x, y)
                nextState = nextState(currentState, self.neighbours(x, y))
                if nextState == Dead and currentState == Alive:
                    self.coords.remove([x, y])
                if nextState == Alive and currentState == Dead:
                    self.coords.append([x, y])
                    
            

    def get(self, x, y):
        print(x, ", ", y)
        print(self.coords)
        if [x, y] in self.coords:
            return Alive
        else:
            return Dead
    

class Test(unittest.TestCase):
    
    # Rule 1
    def testLiving_Cell_Zero_Neighbour_Dead(self):
        self.assertEqual(nextState(Alive, 0), Dead)
    def testLiving_Cell_One_Neighbour_Dead(self):
        self.assertEqual(nextState(Alive, 1), Dead)

    # Rule 2
    def testLiving_Cell_Two_Neighbours_Alive(self):
        self.assertEqual(nextState(Alive, 2), Alive)
    def testLiving_Cell_Three_Neighbours_Alive(self):
        self.assertEqual(nextState(Alive, 3), Alive)
    
    # Rule 3    
    def testLiving_Cell_Four_Neighbours_Dead(self):
        self.assertEqual(nextState(Alive, 4), Dead)
        
    # Rule 4
    def testDead_Cell_Three_Neighbours_Alive(self):
        self.assertEqual(nextState(Dead, 3), Alive)
    def testDead_Cell_Two_Neighbours_Dead(self):
        self.assertEqual(nextState(Dead, 2), Dead)
    
    
    def testWorld_2Neighbour(self):
        world = World()
        world.activate(0,0)
        world.activate(0, 1)
        world.activate(1, 0)
        self.assertEqual(world.neighbours(0, 0), 2)
        self.assertEqual(world.neighbours(1, 0), 2)
        self.assertEqual(world.neighbours(0, 1), 2)
    def testWorld_ThreeCells_OneLives(self):
        world = World()
        world.activate(1, 0)
        world.activate(1, 1)
        world.activate(0, 1)
        world.nextGeneration
        self.assertEqual(world.get(0, 0), Alive)
        
    def testWorld_getMethod(self):
        world = World()
        self.assertEqual(world.get(0, 0), Dead)
    def testWorld_Test(self):
        world = World()
        world.activate(0, 0)
        world.nextGeneration
        self.assertEqual(world.get(0, 0), Dead)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLiving_Cell_One_Neighbour_Dies']
    unittest.main()