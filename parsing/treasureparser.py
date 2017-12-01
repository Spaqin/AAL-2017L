from datastructures.treasure import Treasure


class TreasureParser(object):

    @staticmethod
    def from_dict(treasure_dict, graph):
        for city, treasure in treasure_dict.items():
            graph.nodes[city]["treasure"] = Treasure(treasure["value"], treasure["size"])
        return graph

    @staticmethod
    def to_dict(graph):
        treasure_dict = dict()
        for node in list(graph.nodes):
            treasure = graph.nodes[node].get("treasure", None)
            if treasure:
                treasure_dict[node] = {"value": treasure.value, "size": treasure.size}
        return treasure_dict
