from generators.graph_generator import GraphGenerator
from generators.treasure_generator import TreasureGenerator
from parsing.problemparser import ProblemParser
from itertools import combinations_with_replacement
import networkx as nx
import random as r


class ProblemGenerator(object):
    def __init__(self, city_count, treasure_count, minimum_paths, maximum_paths, seed=None):
        r.seed(seed)
        self.graph_gen = GraphGenerator(city_count, minimum_paths, maximum_paths, r)
        self.treasure_gen = TreasureGenerator(treasure_count, r)
        self.graph = None
        self.treasure_list = None
        self.trunk_size = 0
        self.start = None
        self.end = None
        
    def generate_problem(self):
        self.graph = self.graph_gen.generate_graph()
        cities = self.graph_gen.cities
        self.treasure_list = self.treasure_gen.generate_treasure_list()
        for treasure in self.treasure_list:
            city = r.choice(cities)
            treasure.city = city
            cities.remove(city)
        self.trunk_size = self.treasure_gen.suggested_trunk_size

        # find some good starting and ending points, from top 3rd of longest paths
        shortest_paths = self.graph.all_pairs_shortest_path_length()
        combs = combinations_with_replacement(self.graph.nodes, 2)
        mapping = []
        for combination in combs:
            mapping.append((combination[0], combination[1], shortest_paths[combination[0]][combination[1]]))
        mapping.sort(key=lambda t: t[2])
        top_third = mapping[len(mapping)/3:]
        self.start, self.end, _ = r.choice(top_third)

    def problem_to_yml(self):
        problem_parser = ProblemParser()
        yml = problem_parser.from_problem(self.graph, self.trunk_size, self.start, self.end, self.treasure_list)
        return yml

