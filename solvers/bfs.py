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
        path = []
        queue = q.Queue()
        queue.put_nowait(self.start)

        while not queue.empty:
            parent = queue.get_nowait()
            if parent == self.end:
                return self.construct_path(parent)

            for child in self.graph.neighbors(parent):
                if child in visited:
                    continue
                if child not in queue:
                    self.meta[child] = parent
                    queue.put_nowait(child)

            visited.add(parent)
        return []

    def construct_path(self, last_state):
        path = []
        current_node = last_state
        while current_node != self.start:
            path.append(current_node)
            current_node = self.meta[current_node]

        return path.reverse()
