import yaml
from parsing.graphparser import graph_to_dict, graph_from_dict
from parsing.treasureparser import treasure_from_dict_to_graph, treasure_from_graph_to_dict, treasure_from_list_to_dict
from datastructures.problem import Problem
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


def problem_from_input(text_in):
    self.problem = yaml.load(text_in)
    pre_graph = graph_from_dict(self.problem["Graph"])
    self.graph = treasure_from_dict_to_graph(self.problem["Treasures"], pre_graph)
    self.trunk_size = self.problem["Trunk_size"]
    self.start = self.problem["Start_city"]
    self.end = self.problem["End_city"]
    return Problem(self.graph, self.start, self.end, self.trunk_size)


def yaml_from_problem(problem):
    final_problem_dict = dict()
    final_problem_dict["Graph"] = graph_to_dict(problem.graph)
    if problem.treasure_list:
        final_problem_dict["Treasures"] = treasure_from_list_to_dict(problem.treasure_list)
    else:
        final_problem_dict["Treasures"] = treasure_from_graph_to_dict(problem.graph)
    final_problem_dict["Trunk_size"] = problem.trunk_size
    final_problem_dict["Start_city"] = problem.start
    final_problem_dict["End_city"] = problem.end
    return yaml.dump(problem)
