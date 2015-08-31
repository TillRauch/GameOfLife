'''
Created on 30.08.2015

@author: Till
'''
import unittest
from source.GoL import Alive, nextState, Dead
from source.world import World




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
    
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLiving_Cell_One_Neighbour_Dies']
    unittest.main()