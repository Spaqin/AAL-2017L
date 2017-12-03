import yaml
from parsing.graphparser import GraphParser
from parsing.treasureparser import TreasureParser

"""
YAMLs are cool, very readable, easily understandable by people who had lil' bit of Python experience,
unlike the big scary XMLs or unclear JSONs
An example yaml file defining the problem:

===================

Graph:
  A: [B, C, D]
  B: [E, G, A]
  C:
    - H

Treasures:
  A:
    value: 15
    size: 40
  C:
    value: 400
    size: 5

Trunk_size: 800

Start_city: C
End_city: A

==================
Quick rundown:

Graph: # dict of nodes
  [Node name - string]: [List of neighbors] # it's ok if they're not unique

Treasures:
  [Node name]:
    value: [integer]
    size: [integer]

Trunk_size: [integer]
Start_city: [string]
End_city: [string]
==================

Final graph will have:
nodes (ie. graph[A]) - treasure info object, so:
"""


class ProblemParser(object):
    def __init__(self):
        self.problem = dict()
        self.graph = None
        self.trunk_size = None
        self.start = None
        self.end = None

    def from_input(self, text_in):
        self.problem = yaml.load(text_in)
        pre_graph = GraphParser.from_dict(self.problem["Graph"])
        self.graph = TreasureParser.from_dict_to_graph(self.problem["Treasures"], pre_graph)
        self.trunk_size = self.problem["Trunk_size"]
        self.start = self.problem["Start_city"]
        self.end = self.problem["End_city"]

    def from_problem(self, graph, trunk_size, start, end, treasure_list=None):
        self.problem["Graph"] = GraphParser.to_dict(graph)
        if treasure_list:
            self.problem["Treasure"] = TreasureParser.from_list_to_dict(treasure_list)
        else:
            self.problem["Treasure"] = TreasureParser.from_graph_to_dict(graph)
        self.problem["Trunk_size"] = trunk_size
        self.problem["Start_city"] = start
        self.problem["End_city"] = end
        return yaml.dump(self.problem)
