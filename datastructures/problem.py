from parsing.treasureparser import treasure_from_list_to_graph


class Problem(object):
    def __init__(self, graph, start, end, trunk_size, treasure_list=None):
        self.graph = graph if not treasure_list else treasure_from_list_to_graph(treasure_list, graph)
        self.start = start
        self.end = end
        self.trunk_size = trunk_size
        self.treasure_list = treasure_list
