from networkx import Graph
import queue as q


class BFS(object):
    def __init__(self, graph, start, end):
        self.graph = graph
        self.meta = dict()
        self.start = start
        self.end = end

    def solve_graph(self):
        visited = set()
        queue = [self.start]
        while len(queue):
            parent = queue.pop(0)
            if parent == self.end:
                return self.construct_path(parent)
            for child in self.graph.neighbors(parent):
                if child in visited:
                    continue
                if child not in queue:
                    self.meta[child] = parent
                    queue.append(child)
            visited.add(parent)
        return []

    def construct_path(self, last_state):
        path = []
        current_node = last_state
        while current_node != self.start:
            path.insert(0, current_node)
            current_node = self.meta[current_node]
        path.insert(0, self.start)
        return path
