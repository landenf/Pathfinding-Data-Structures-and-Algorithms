import unittest
import f_w as fw

class TestFloydWarshall(unittest.TestCase):

    def setUp(self):
        self.graph_matrix, self.vertices = fw.create_graph_matrix(0)
        self.updated_matrix = fw.floyd_warshall(self.graph_matrix)

    def test_create_graph_matrix(self):
        self.assertEqual(len(self.graph_matrix), self.vertices)
        for row in self.graph_matrix:
            self.assertEqual(len(row), self.vertices)

    def test_floyd_warshall(self):
        expected_result = [[0, 282.842712474619, 482.842712474619], [282.842712474619, 0, 200.0], [482.842712474619, 200.0, 0]]
        print(self.updated_matrix)
        self.assertEqual(self.updated_matrix, expected_result)

    def test_build_paths(self):
        parent_matrix = fw.build_paths(self.updated_matrix)
        expected_result = [[-1, 0, 0], [1, -1, 1], [2, 2, -1]]
        self.assertEqual(parent_matrix, expected_result)

if __name__ == '__main__':
    unittest.main()
