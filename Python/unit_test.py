import math
import unittest
import pathing
import graph_data
import global_game_data

class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)
    
    # BFS Unit Test -- Graph 3 Target 8
    def test_get_bfs_path(self):
        graph = graph_data.graph_data[3]
        target = 8
        expected_path = [0,4,8,9,10,11,15]
        actual = pathing.get_bfs_path(graph, target)
        self.assertEqual(actual, expected_path)
    
        # DFS Unit Test -- Graph 3 Target 7
    def test_get_bfs_path2(self):
        graph = graph_data.graph_data[3] 
        target = 7 
        expected_path = [0, 1, 2,3,7,11,15]
        actual = pathing.get_bfs_path(graph, target)  
        self.assertEqual(actual, expected_path)

        # BFS Unit Test -- Graph 2 Target 5
    def test_get_bfs_path3(self):
        graph = graph_data.graph_data[2]
        target = 5
        expected_path = [0,21,5,21,23]
        actual = pathing.get_bfs_path(graph, target)
        self.assertEqual(actual, expected_path)
    
        # BFS Unit Test -- Graph 2 Target 10
    def test_get_bfs_path4(self):
        graph = graph_data.graph_data[2]  
        target = 10  
        expected_path = [0,17,15,10,5,21,23]
        actual = pathing.get_bfs_path(graph, target)  
        self.assertEqual(actual, expected_path)

       # DFS Unit Test -- Graph 2 Target 8
    def test_get_dfs_path(self):
        graph = graph_data.graph_data[3]
        target = 8
        expected_path = [0,1,2,3,7,6,5,4,8,9,10,11,15]
        actual = pathing.get_dfs_path(graph, target)
        self.assertEqual(actual, expected_path)
    
        # DFS Unit Test -- Graph 3 Target 7
    def test_get_dfs_path2(self):
        graph = graph_data.graph_data[3] 
        target = 7 
        expected_path = [0,1,2,3,7,6,5,4,8,9,10,11,15]
        actual = pathing.get_dfs_path(graph, target)  
        self.assertEqual(actual, expected_path)

        # DFS Unit Test -- Graph 2 Target 8
    def test_get_dfs_path3(self):
        graph = graph_data.graph_data[2]
        target = 8
        expected_path = [0, 17, 11, 3, 8, 3, 6, 4, 7, 1, 2, 5, 10, 9, 12, 11, 16, 17, 15, 14, 18, 23]
        actual = pathing.get_dfs_path(graph, target)
        self.assertEqual(actual, expected_path)
    
    # DFS Unit Test -- Graph 2 Target 3
    def test_get_dfs_path4(self):
        graph = graph_data.graph_data[2]  
        target = 3 
        expected_path = [0, 17, 11, 3, 6, 4, 7, 1, 2, 5, 10, 9, 12, 11, 16, 17, 15, 14, 18, 23]
        actual = pathing.get_dfs_path(graph, target)  
        self.assertEqual(actual, expected_path)

    #Check if the function produces the correct distance dictionary for a simple graph.
    def test_distance_dictionary(self):
        graph_data = [
            [(0, 0), {1}],
            [(1, 0), {0, 2}],
            [(2, 0), {1}]
        ]
        result_dict = pathing.get_distance_dictionary(graph_data)
        expected_dict = {0: {1: 1.0}, 1: {0: 1.0, 2: 1.0}, 2: {1: 1.0}}
        self.assertEqual(result_dict, expected_dict)
    
     #Check if the function handles an empty graph correctly.
    def test_empty_graph(self):
        graph_data = []
        result_dict = pathing.get_distance_dictionary(graph_data)
        expected_dict = {}
        self.assertEqual(result_dict, expected_dict)
        
    #Check if the function calculates the distance correctly for two points.
    def test_distance_calculation(self):
        coord1 = (0, 0)
        coord2 = (3, 4)
        result_distance = pathing.calculate_distance(coord1, coord2)
        expected_distance = 5.0
        self.assertEqual(result_distance, expected_distance)

    #Check if the function returns 0 for the distance between identical coordinates.
    def test_same_coordinates(self):
        coord1 = (2, 5)
        coord2 = (2, 5)
        result_distance = pathing.calculate_distance(coord1, coord2)
        expected_distance = 0.0
        self.assertEqual(result_distance, expected_distance)    

    def test_dijkstra_graph_0(self):
        graph = graph_data.graph_data[0]  
        target = 1
        expected_path = [0,1,2]
        result_path = pathing.get_dijkstra_path(graph,target)
        expected_path = [0, 1, 2]
        self.assertEqual(result_path, expected_path)

    def test_dijkstra_graph_1(self):
        graph = graph_data.graph_data[1]  
        target = 2
        expected_path = [0,1,2,3]

        result_path = pathing.get_dijkstra_path(graph,target)
        self.assertEqual(result_path, expected_path)

    def test_dijkstra_graph_2(self):
        graph = graph_data.graph_data[3]  
        target = 7
        expected_path = [0,1,2,3,7,11,15]

        result_path = pathing.get_dijkstra_path(graph,target)
        self.assertEqual(result_path, expected_path)

if __name__ == '__main__':
    unittest.main()

