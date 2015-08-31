'''
Created on 31.08.2015

@author: Till
'''
import unittest
from source.world import World
from source.GoL import Alive, Dead


class Test(unittest.TestCase):


    def testWorld_nextGenUpdatesWorldAllTogether(self):
        world = World()
        world.activate(1, 1)
        world.activate(3, 1)
        world.activate(2, 2)
        world.nextGeneration()
        self.assertEqual(world.get(2, 1), Alive)
    def testWorld_2Neighbour(self):
        world = World()
        world.activate(1,1)
        world.activate(1, 2)
        world.activate(2, 1)
        self.assertEqual(world.neighbours(1, 1), 2)
        self.assertEqual(world.neighbours(2, 1), 2)
        self.assertEqual(world.neighbours(1, 2), 2)
    def testWorld_ThreeCells_OneLives(self):
        world = World()
        world.activate(2, 1)
        world.activate(2, 2)
        world.activate(1, 2)
        world.nextGeneration()
        self.assertEqual(world.get(1, 1), Alive)
        
    def testWorld_getMethod(self):
        world = World()
        self.assertEqual(world.get(1, 1), Dead)
    def testWorld_Test(self):
        world = World()
        world.activate(1, 1)
        world.nextGeneration()
        self.assertEqual(world.get(1, 1), Dead)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()