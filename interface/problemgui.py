import matplotlib.pyplot as pl
import networkx.drawing as nx


def create_plot(graph, path, treasure_list):
    treasure_cities = [n.city for n in treasure_list]
    node_colors = ["green" if n in treasure_cities and n in path else "blue" if n in path else "red" for n in graph.nodes()]
    for i in range(len(path)):
        graph[path[i]][path[i+1]]["color"] = "blue"
    edge_colors = [graph[e[0]][e[1]].get("color", "black") for e in graph.edges()]
    