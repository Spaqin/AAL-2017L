import matplotlib.pyplot as pl
import networkx.drawing as nx
from parsing.treasureparser import treasure_from_list_to_dict


def draw_plot(problem, path, to_take):
    node_labels = dict()
    treasure_cities = treasure_from_list_to_dict(to_take)

    for node in problem.graph.nodes():
        n = problem.graph.nodes[node]
        if n.get("treasure") and node in path:
            node_labels[node] = "{}\ns:{}/v:{}".format(
                node, n["treasure"].size, n["treasure"].value)
        else:
            node_labels[node] = node

    # node colors
    node_colors = ["orange" if n in [problem.start, problem.end] and n in treasure_cities.keys()
                   else "yellow" if n in [problem.start, problem.end]
                   else "#CCFFCC" if n in treasure_cities.keys() and n in path
                   else "#CCCCFF" if n in path
                   else "#FFCCCC"
                   for n in problem.graph.nodes()]

    # edge colors
    for i in range(len(path)-1):
        problem.graph[path[i]][path[i+1]]["color"] = "blue"
        problem.graph[path[i]][path[i+1]]["weight"] = 2.0
    edge_colors = [problem.graph[e[0]][e[1]].get("color", "black") for e in problem.graph.edges()]
    edge_weights = [problem.graph[e[0]][e[1]].get("weight", 0.5) for e in problem.graph.edges()]

    nx.draw_networkx(problem.graph,
                     alpha=0.7,
                     node_color=node_colors,
                     edge_color=edge_colors,
                     width=edge_weights,
                     labels=node_labels,
                     font_size=10,
                     font_weight="bold")
    pl.show()
