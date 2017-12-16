from generators.problem_generator import ProblemGenerator
from parsing.problemparser import yaml_from_problem

from sys import stderr
from plumbum import cli
from time import perf_counter
import logging


class GeneratorApplication(cli.Application):
    """Creates a problem, throws it on stdout and quits.
    Just like me with my life."""
    city_count = 25
    min_edges = 1
    max_edges = 3
    treasure_count = 20
    seed = None
    force_longest_paths = False

    @cli.switch(["-c", "--city-count"], int)
    def set_city_count(self, city_count):
        """Sets generated city count (default - 25)"""
        self.city_count = city_count

    @cli.switch(["-f", "--force-longests"])
    def force_longest_paths(self):
        """Forces to choose from longest paths (warning: may take a long time)"""
        self.force_longest_paths = True

    @cli.switch(["-l", "--min-edges"], int)
    def set_min_edges(self, edges):
        """Sets minimum edge count per node in the graph (default - 1)"""
        self.min_edges = edges

    @cli.switch(["-h", "--max-edges"], int)
    def set_max_edges(self, edges):
        """Sets maximum edge count per node in the graph (default - 3)"""
        self.max_edges = edges

    @cli.switch(["-t", "--treasure-count"], int)
    def set_treasure_count(self, treasures):
        """Sets maximum edge count per node in the graph (default - 20)"""
        self.treasure_count = treasures

    @cli.switch(["-s", "--seed"], int)
    def set_seed(self, seed):
        """Sets seed for pseudo-random number generator"""
        self.seed = seed

    def main(self):
        logging.basicConfig(level=logging.INFO)
        prob_gen = ProblemGenerator(self.city_count, self.treasure_count, self.min_edges, self.max_edges, self.seed)
        start = perf_counter()
        problem = prob_gen.generate_problem(self.force_longest_paths)
        end = perf_counter()
        logging.info("Generation took {:06.10f}s".format(end-start))
        yml = yaml_from_problem(problem)
        print(yml)


if __name__ == "__main__":
    GeneratorApplication.run()
