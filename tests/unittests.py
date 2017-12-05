import unittest
from parsing.problemparser import ProblemParser,TreasureParser
from solvers.graph.dijkstra import Dijkstra
from solvers.graph.bfs import BFS
from solvers.knapsack.mitm import meet_in_the_middle
from solvers.knapsack.greedy import greedy
from generators import problem_generator


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
        self.assertTrue(solved == ['Ulsan', 'Daegu', 'Gumi', 'Seoul', 'Pyeongyang']
                        or solved == ['Ulsan', 'Daegu', 'Daejeon', 'Seoul', 'Pyeongyang'])

    def dijkstra(self):
        with open("tests/test.yml") as f:
            str = f.read()
        pp = ProblemParser()
        pp.from_input(str)
        dijkstra = Dijkstra(pp.graph, pp.start, pp.end)
        solved = dijkstra.solve_graph()
        print(solved)
        self.assertTrue(solved == ['Ulsan', 'Daegu', 'Gumi', 'Seoul', 'Pyeongyang']
                        or solved == ['Ulsan', 'Daegu', 'Daejeon', 'Seoul', 'Pyeongyang'])

    def mitm(self):
        with open("tests/test.yml") as f:
            str = f.read()
        pp = ProblemParser()
        pp.from_input(str)
        dijkstra = Dijkstra(pp.graph, pp.start, pp.end)
        solved = dijkstra.solve_graph()
        print(solved)
        tr_list = TreasureParser.from_graph_with_path(pp.graph, solved)
        print("treasures: ", tr_list)
        to_take = meet_in_the_middle(tr_list, pp.trunk_size)
        print("take: ", to_take)
        self.assertEqual(sum(taken.value for taken in to_take), 766 if "Gumi" in solved else 720)
        self.assertLessEqual(sum(taken.size for taken in to_take), pp.trunk_size)

    def greedy(self):
        with open("tests/test.yml") as f:
            str = f.read()
        pp = ProblemParser()
        pp.from_input(str)
        dijkstra = Dijkstra(pp.graph, pp.start, pp.end)
        solved = dijkstra.solve_graph()
        print(solved)
        tr_list = TreasureParser.from_graph_with_path(pp.graph, solved)
        print("treasures: ", tr_list)
        to_take = greedy(tr_list, pp.trunk_size)
        print("take: ", to_take)
        self.assertEqual(sum(taken.value for taken in to_take), 766 if "Gumi" in solved else 720)
        self.assertLessEqual(sum(taken.size for taken in to_take), pp.trunk_size)

    def generate(self):
        pg = problem_generator.ProblemGenerator(2500, 1500, 1, 5)
        problem = pg.generate_problem()
        yml = pg.problem_to_yml()
        pp = ProblemParser()
        print(yml)
        problem_from_yml = pp.from_input(yml)
        self.assertEqual(problem.graph.number_of_nodes(), problem_from_yml.graph.number_of_nodes())
        self.assertEqual(problem.graph.number_of_edges(), problem_from_yml.graph.number_of_edges())


if __name__ == '__main__':
    unittest.main()