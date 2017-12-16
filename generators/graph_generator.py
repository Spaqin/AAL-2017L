from networkx import Graph
from string import ascii_lowercase
from itertools import product
import gc


class GraphGenerator(object):
    @staticmethod
    def iter_all_strings():
        # handy little generator for city names
        size = 1
        while True:
            for s in product(ascii_lowercase, repeat=size):
                yield "".join(s).capitalize()
            size += 1

    def __init__(self, city_count, minimum_paths, maximum_paths, random):
        self.node_count = city_count
        self.min_paths = minimum_paths
        self.max_paths = maximum_paths
        self.random = random
        self.cities = []

    def generate_graph(self):
        graph = Graph()
        # populate cities:
        g = self.iter_all_strings()
        for _ in range(self.node_count):
            self.cities.append(next(g))

        # to make a connected graph, all nodes should be connected.
        connected = self.cities[:1]
        not_connected = self.cities[1:]

        for city in not_connected:
            connected_with = self.random.choice(connected)
            graph.add_edge(connected_with, city)
            # if the number of neighbors (edges) for connecting city is over max_path, remove it from connected,
            # so it doesn't overflow no more.
            if len(list(graph.neighbors(connected_with))) == self.max_paths:
                connected.remove(connected_with)
            connected.append(city)

        for city in connected:
            neighbors = list(graph.neighbors(city))
            edge_count = self.random.randint(self.min_paths-len(neighbors), self.max_paths-len(neighbors))
            if edge_count < 1:
                continue

            connectable = [c for c in connected if c not in neighbors and c != city]
            if not connectable:
                continue
            for _ in range(edge_count):
                if not connectable:
                    break
                connected_with = self.random.choice(connectable)

                if len(list(graph.neighbors(connected_with))) >= self.max_paths:
                    connectable.remove(connected_with)
                    continue
                graph.add_edge(city, connected_with)
                # same applies, so when we reach max path, remove it from the connectable pool
                connectable.remove(connected_with)
            gc.collect()
        return graph

