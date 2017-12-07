from datastructures.treasure import Treasure


def treasure_from_dict_to_graph(treasure_dict, graph):
    for city, treasure in treasure_dict.items():
        graph.nodes[city]["treasure"] = Treasure(treasure["value"], treasure["size"], city)
    return graph


def treasure_from_graph_to_dict(graph):
    treasure_dict = dict()
    for node in graph.nodes:
        treasure = graph.nodes[node].get("treasure", None)
        if treasure:
            treasure_dict[node] = {"value": treasure.value, "size": treasure.size}
    return treasure_dict


def treasure_from_list_to_dict(treasure_list):
    treasure_dict = dict()
    for treasure in treasure_list:
        treasure_dict[treasure.city] = {"value": treasure.value, "size": treasure.size}
    return treasure_dict


def treasure_from_list_to_graph(treasure_list, graph):
    for treasure in treasure_list:
        graph.nodes[treasure.city]["treasure"] = treasure
    return graph


def treasure_from_dict_to_list(treasure_dict):
    treasure_list = []
    for city in treasure_dict:
        treasure_list.append(Treasure(value=treasure_dict[city]["value"],
                                      size=treasure_dict[city]["size"],
                                      city=city))
    return treasure_list


def treasure_from_graph_with_path(graph, path):
    treasure_list = []
    for city in path:
        treasure = graph.nodes[city].get("treasure")
        if treasure:
            treasure_list.append(treasure)
    return treasure_list
