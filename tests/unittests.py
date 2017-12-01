import unittest
from parsing.problemparser import ProblemParser
from solvers.dijkstra import Dijkstra
from solvers.bfs import BFS

class Tests(unittest.TestCase):
    def parser(self):
        with open("tests/test.yml") as f:
            str = f.read()
        pp = ProblemParser()
        pp.from_input(str)
        print(pp.graph.nodes, pp.graph.edges, pp.start, pp.end, pp.trunk_size)
        for node in pp.graph.nodes:
            print(pp.graph.nodes[node].get("treasure", None))
        self.assertEqual(pp.start, "C")
        self.assertEqual(pp.end, "A")

    def bfs(self):
        with open("tests/test.yml") as f:
            str = f.read()
        pp = ProblemParser()
        pp.from_input(str)
        bfs = BFS(pp.graph, pp.start, pp.end)
        solved = bfs.solve_graph()
        print(solved)
        self.assertEqual(solved, ['H', 'C', 'A', 'D'])


    def dijkstra(self):
        with open("tests/test.yml") as f:
            str = f.read()
        pp = ProblemParser()
        pp.from_input(str)
        dijkstra = Dijkstra(pp.graph, pp.start, pp.end)
        solved = dijkstra.solve_graph()
        print(solved)
        self.assertEqual(solved, ['H', 'C', 'A', 'D'])

if __name__ == '__main__':
    unittest.main()