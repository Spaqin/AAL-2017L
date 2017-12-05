class Problem(object):
    def __init__(self, graph, start, end, trunk_size, treasure_list=None):
        self.graph = graph
        self.start = start
        self.end = end
        self.trunk_size = trunk_size
        self.treasure_list = treasure_list
