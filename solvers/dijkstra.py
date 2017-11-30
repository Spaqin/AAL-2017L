from networkx import Graph

g = Graph


class Dijkstra(object):
    def __init__(self, graph, start, end, distance=1):
        self.graph = graph
        self.meta = dict()
        self.start = start
        self.end = end
        self.DISTANCE = distance  # distance between nodes is const

    def solve_graph(self):
        unvisited = list(self.graph.nodes)
        dist = dict()
        prev = dict()
        for node in unvisited:
            # distance to the end node cannot be longer than number of nodes*dist
            dist[node] = self.graph.number_of_nodes()*self.DISTANCE + 1
            prev[node] = None
            # TODO everything