import math
import unittest
import pathing
import graph_data
import global_game_data
import permutation

class TestPermutations(unittest.TestCase):

    #Thease unit tests, test if the correct output is given. 
    #Per spec the output should be all the possible permutations from 1 to n-1 
    #keeping constant the start and end node. 
    def test_permutation_3(self):
        expected = [[1, 2, 3]]
        actual = permutation.main(3)
        self.assertEqual(expected, actual)

    def test_permutation_4(self):
        expected = [[1,2,3,4],[1,3,2,4]] 
        actual = permutation.main(4)
        self.assertEqual(expected, actual)

    def test_permutation_5(self):
        expected = [[1, 2, 3, 4, 5], [1, 2, 4, 3, 5], [1, 4, 2, 3, 5], [1, 4, 3, 2, 5], [1, 3, 4, 2, 5], [1, 3, 2, 4, 5]]
        actual = permutation.main(5)
        self.assertEqual(expected, actual)

    #Thease unit tests, test the edge case (-1)
    def test_permutation_5(self):
        expected = False
        actual = permutation.main(2)
        self.assertEqual(expected, actual)

    #Thease unit tests, test the helper functions
    def test_findNum(self):
        Array = [1, 2, 3, 4, 5]
        num = 3
        length = len(Array)
        result = permutation.findNum(Array, num, length)
        self.assertEqual(result, 3)  

    def test_findMobile(self):
        NodeArray = [1, 3, 2, 4, 5]
        DirectionArray = [1, 0, 1, 0, 1] 
        length = len(NodeArray)
        result = permutation.findMobile(NodeArray, DirectionArray, length)
        self.assertEqual(result, 4)  


if __name__ == '__main__':
    unittest.main()
