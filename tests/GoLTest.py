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
        world.activate(0, 0)
        world.activate(2, 0)
        world.activate(1, 1)
        world.nextGeneration()
        self.assertEqual(world.get(1, 0), Alive)
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
        world.nextGeneration()
        self.assertEqual(world.get(0, 0), Alive)
        
    def testWorld_getMethod(self):
        world = World()
        self.assertEqual(world.get(0, 0), Dead)
    def testWorld_Test(self):
        world = World()
        world.activate(0, 0)
        world.nextGeneration()
        self.assertEqual(world.get(0, 0), Dead)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()