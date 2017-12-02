from networkx import Graph

g = Graph


class Dijkstra(object):
    def __init__(self, graph, start, end, distance=1):
        self.graph = graph
        self.meta = dict()
        self.start = start
        self.end = end
        self.DISTANCE = distance  # default distance between nodes if undefined
        self.prev = dict()

    def solve_graph(self):
        unvisited = list(self.graph.nodes)
        dist = dict()
        for node in unvisited:
            # distance to the end node cannot be longer than number of nodes*dist... if dist is const
            # else this may fail. to make sure, we square it
            dist[node] = (self.graph.number_of_nodes()*self.DISTANCE)**2 + 1
            self.prev[node] = None

        dist[self.start] = 0

        while len(unvisited) > 0:
            min_val = (self.graph.number_of_nodes()*self.DISTANCE)**2 + 1
            u = None
            for unvis_key in unvisited:
                if dist[unvis_key] < min_val:
                    min_val = dist[unvis_key]
                    u = unvis_key

            unvisited.remove(u)

            if u == self.end:
                return self.construct_path(u)

            for neighbor in self.graph.neighbors(u):
                cost = self.graph[u][neighbor].get("cost", self.DISTANCE)
                temp = dist[u] + cost
                if temp < dist[neighbor]:
                    dist[neighbor] = temp
                    self.prev[neighbor] = u

    def construct_path(self, state):
        path = list()
        u = self.end
        while self.prev[u]:
            path.insert(0, u)
            u = self.prev[u]
        path.insert(0, u)
        return path
