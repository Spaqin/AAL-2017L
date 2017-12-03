from networkx import Graph
from string import ascii_lowercase
from itertools import product


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

    def create_graph(self):
        graph = Graph()
        # populate cities:
        for _ in range(self.node_count):
            self.cities.append(next(self.iter_all_strings()))

        # to make a connected graph, all nodes should be connected.
        connected = self.cities[:1]
        not_connected = self.cities[1:]

        for city in not_connected:
            connected_with = self.random.choice(connected)
            graph.add_edge(connected_with, city)
            # if the number of neighbors (edges) for connecting city is over max_path, remove it from connected,
            # so it doesn't overflow no more.
            if len(graph.neighbors(connected_with)) >= self.max_paths:
                connected.remove(connected_with)
            connected.append(city)

        for city in connected:
            neighbors = graph.neighbors(city)
            edge_count = self.random.randint(self.min_paths-len(neighbors), self.max_paths)
            if edge_count < 1:
                continue
            connectable = [c for c in connected if c not in neighbors and c != city]
            for _ in range(edge_count):
                connected_with = self.random.choice(connectable)
                graph.add_edge(city, connected_with)
                # same applies, so when we reach max path, remove it from the connectable pool
                if len(graph.neighbors(connected_with)) >= self.max_paths:
                    connected.remove(connected_with)
                connectable.remove(connected_with)

        return graph

