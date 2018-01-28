import unittest
from graph_generator import GraphGenerator


class TestGraphGenerator(unittest.TestCase):
    def setUp(self):
        self.g = GraphGenerator()

    def test_are_nodes_connected(self):
        self.g.graph = {
            '1': ['2'],
            '2': ['1']
        }
        self.assertTrue(self.g.are_nodes_connected('1', '2'))
        self.g.graph = {
            '1': ['2'],
            '2': ['3', '1'],
            '3': ['2']
        }
        self.assertTrue(self.g.are_nodes_connected('1', '3'))
        self.g.graph = {
            '1': ['2', '3'],
            '2': ['3'],
            '3': ['4'],
            '4': ['3']
        }
        self.assertTrue(self.g.are_nodes_connected('1', '4'))
        self.g.graph = {
            '1': ['2', '3'],
            '2': ['3'],
            '3': ['1'],
            '4': []
        }
        self.assertFalse(self.g.are_nodes_connected('1', '4'))

    def test_has_cycles(self):
        self.g.graph = {
            '1': ['2'],
            '2': ['1'],
        }
        self.assertFalse(self.g.has_cycles())
        self.g.graph = {
            '1': ['2', '3'],
            '2': ['3'],
            '3': ['1'],
            '4': []
        }
        self.assertTrue(self.g.has_cycles())
        self.g.graph = {
            '1': ['2', '3'],
            '2': ['3'],
            '3': ['4'],
            '4': []
        }
        self.assertFalse(self.g.has_cycles())

    def test_are_all_nodes_connected(self):
        self.g.graph = {
            '1': ['2', '3'],
            '2': ['3'],
            '3': ['1'],
            '4': []
        }
        self.assertFalse(self.g.are_all_nodes_connected())
        self.g.graph = {
            '1': ['2', '3'],
            '2': ['3', '1'],
            '3': ['4', '2', '1'],
            '4': ['3']
        }
        self.assertTrue(self.g.are_all_nodes_connected())

    def test_is_tree(self):
        graph = {
            '1': ['2', '3'],
            '2': ['3'],
            '3': ['1'],
            '4': []
        }
        self.assertFalse(GraphGenerator.is_tree(graph))
        graph = {
            '1': ['2', '3'],
            '2': ['1'],
            '3': ['4', '1'],
            '4': ['3']
        }
        self.assertTrue(GraphGenerator.is_tree(graph))


if __name__ == '__main__':
    unittest.main()
