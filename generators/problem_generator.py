from generators.graph_generator import GraphGenerator
from generators.treasure_generator import TreasureGenerator


class ProblemGenerator(object):
    def __init__(self, city_count, treasure_count, minimum_paths, maximum_paths, seed=None):
        self.graph_gen = GraphGenerator(city_count, minimum_paths, maximum_paths, seed)
        self.treasure_gen = TreasureGenerator(treasure_count, seed)
