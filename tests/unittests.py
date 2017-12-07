import unittest
from parsing.problemparser import yaml_from_problem, problem_from_input
from parsing import treasureparser
from solvers.graph.dijkstra import Dijkstra
from solvers.graph.bfs import BFS
from solvers.knapsack.mitm import meet_in_the_middle
from solvers.knapsack.greedy import greedy
from interface import problemgui
from generators import problem_generator


class Tests(unittest.TestCase):
    def parser(self):
        with open("tests/test.yml") as f:
            str = f.read()
        pp = problem_from_input(str)
        print(pp.graph.nodes, pp.graph.edges, pp.start, pp.end, pp.trunk_size)
        for node in pp.graph.nodes:
            print(pp.graph.nodes[node].get("treasure", None))
        self.assertEqual(pp.start, "Ulsan")
        self.assertEqual(pp.end, "Pyeongyang")

    def bfs(self):
        with open("tests/test.yml") as f:
            str = f.read()
        pp = problem_from_input(str)
        bfs = BFS(pp)
        solved = bfs.solve_graph()
        print(solved)
        self.assertTrue(solved == ['Ulsan', 'Daegu', 'Gumi', 'Seoul', 'Pyeongyang']
                        or solved == ['Ulsan', 'Daegu', 'Daejeon', 'Seoul', 'Pyeongyang'])

    def dijkstra(self):
        with open("tests/test.yml") as f:
            str = f.read()
        pp = problem_from_input(str)
        dijkstra = Dijkstra(pp)
        solved = dijkstra.solve_graph()
        print(solved)
        self.assertTrue(solved == ['Ulsan', 'Daegu', 'Gumi', 'Seoul', 'Pyeongyang']
                        or solved == ['Ulsan', 'Daegu', 'Daejeon', 'Seoul', 'Pyeongyang'])

    def mitm(self):
        with open("tests/test.yml") as f:
            str = f.read()
        pp = problem_from_input(str)
        dijkstra = Dijkstra(pp)
        solved = dijkstra.solve_graph()
        print(solved)
        pp.treasure_list = treasureparser.treasure_from_graph_with_path(pp.graph, solved)
        print("treasures: ", pp.treasure_list)
        treasure_list = treasureparser.treasure_from_graph_with_path(pp.graph, solved)
        to_take = meet_in_the_middle(treasure_list, pp.trunk_size)
        print("take: ", to_take)
        self.assertEqual(sum(taken.value for taken in to_take), 766 if "Gumi" in solved else 720)
        self.assertLessEqual(sum(taken.size for taken in to_take), pp.trunk_size)

    def greedy(self):
        with open("tests/test.yml") as f:
            str = f.read()
        pp = problem_from_input(str)
        dijkstra = Dijkstra(pp)
        solved = dijkstra.solve_graph()
        print(solved)
        pp.treasure_list = treasureparser.treasure_from_graph_with_path(pp.graph, solved)
        print("treasures: ", pp.treasure_list)
        treasure_list = treasureparser.treasure_from_graph_with_path(pp.graph, solved)
        to_take = greedy(treasure_list, pp.trunk_size)
        print("take: ", to_take)
        self.assertEqual(sum(taken.value for taken in to_take), 766 if "Gumi" in solved else 720)
        self.assertLessEqual(sum(taken.size for taken in to_take), pp.trunk_size)

    def generate(self):
        pg = problem_generator.ProblemGenerator(25, 15, 1, 3)
        problem = pg.generate_problem()
        yml = yaml_from_problem(problem)
        print(yml)
        problem_from_yml = problem_from_input(yml)
        self.assertEqual(problem.graph.number_of_nodes(), problem_from_yml.graph.number_of_nodes())
        self.assertEqual(problem.graph.number_of_edges(), problem_from_yml.graph.number_of_edges())

    def draw(self):
        with open("tests/test.yml") as f:
            str = f.read()
        pp = problem_from_input(str)
        dijkstra = Dijkstra(pp)
        solved = dijkstra.solve_graph()
        treasure_list = treasureparser.treasure_from_graph_with_path(pp.graph, solved)
        to_take = greedy(treasure_list, pp.trunk_size)
        problemgui.draw_plot(pp, solved, to_take)

    def generate_and_draw(self):
        pg = problem_generator.ProblemGenerator(25, 18, 1, 40)
        problem = pg.generate_problem()
        dijkstra = Dijkstra(problem)
        solved = dijkstra.solve_graph()
        treasure_list = treasureparser.treasure_from_graph_with_path(problem.graph, solved)
        to_take = meet_in_the_middle(treasure_list, problem.trunk_size)
        problemgui.draw_plot(problem, solved, to_take)


if __name__ == '__main__':
    unittest.main()