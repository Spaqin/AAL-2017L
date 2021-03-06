from generators.graph_generator import GraphGenerator
from generators.treasure_generator import TreasureGenerator
from parsing.problemparser import yaml_from_problem
from datastructures.problem import Problem
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
        self.problem = None

    def generate_problem(self, force_top_longest=True):
        self.graph = self.graph_gen.generate_graph()
        cities = self.graph_gen.cities
        self.treasure_list = self.treasure_gen.generate_treasure_list()
        for treasure in self.treasure_list:
            city = r.choice(cities)
            treasure.city = city
            cities.remove(city)
        self.trunk_size = self.treasure_gen.suggested_trunk_size
        if force_top_longest:
            # find some good starting and ending points, from top 3rd of longest paths
            shortest_paths = dict(nx.all_pairs_shortest_path_length(self.graph))
            combs = list(combinations_with_replacement(self.graph.nodes, 2))
            mapping = []
            for combination in combs:
                mapping.append((combination[0], combination[1], shortest_paths[combination[0]][combination[1]]))
            mapping.sort(key=lambda t: t[2])

            # top 20 or top third, what's lower
            top_number = min(20, len(mapping) // 3)
            top_longest = mapping[-top_number:]
            self.start, self.end, _ = r.choice(top_longest)
        else:
            self.start = r.choice(list(self.graph.nodes()))
            self.end = r.choice(list(self.graph.nodes()))

        self.problem = Problem(self.graph, self.start, self.end, self.trunk_size, self.treasure_list)

        return self.problem

    def problem_to_yml(self):
        yml = yaml_from_problem(self.problem)
        return yml

