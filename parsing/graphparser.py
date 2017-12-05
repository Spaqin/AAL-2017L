from networkx import Graph


class GraphParser(object):

    @staticmethod
    def from_dict(graph_dict):
        graph = Graph()
        for node, neighbor_list in graph_dict.items():
            for neighbor in neighbor_list:
                graph.add_edge(node, neighbor)
        return graph

    @staticmethod
    def to_dict(graph):
        ret_dict = dict()
        for node in graph.nodes:
            ret_dict[node] = list(graph.neighbors(node))
        return ret_dict
