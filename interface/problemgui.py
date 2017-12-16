import matplotlib.pyplot as pl
import networkx.drawing as nx
from parsing.treasureparser import treasure_from_list_to_dict


def draw_plot(solution):
    node_labels = dict()
    treasure_cities = treasure_from_list_to_dict(solution.to_take)

    for node in solution.problem.graph.nodes():
        n = solution.problem.graph.nodes[node]
        if n.get("treasure") and node in solution.path:
            node_labels[node] = "{}\ns:{}/v:{}".format(
                node, n["treasure"].size, n["treasure"].value)
        else:
            node_labels[node] = node

    # node colors
    node_colors = ["orange" if n in [solution.problem.start, solution.problem.end] and n in treasure_cities.keys()
                   else "yellow" if n in [solution.problem.start, solution.problem.end]
                   else "#CCFFCC" if n in treasure_cities.keys() and n in solution.path
                   else "#CCCCFF" if n in solution.path
                   else "#FFCCCC"
                   for n in solution.problem.graph.nodes()]

    # edge colors
    for i in range(len(solution.path)-1):
        solution.problem.graph[solution.path[i]][solution.path[i+1]]["color"] = "blue"
        solution.problem.graph[solution.path[i]][solution.path[i+1]]["weight"] = 2.0
    edge_colors = [solution.problem.graph[e[0]][e[1]].get("color", "black") for e in solution.problem.graph.edges()]
    edge_weights = [solution.problem.graph[e[0]][e[1]].get("weight", 0.5) for e in solution.problem.graph.edges()]

    nx.draw_networkx(solution.problem.graph,
                     alpha=0.7,
                     node_color=node_colors,
                     edge_color=edge_colors,
                     width=edge_weights,
                     labels=node_labels,
                     font_size=10,
                     font_weight="bold")
    pl.show()
