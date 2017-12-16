from parsing import problemparser, treasureparser
from interface import problemgui
from datastructures.solution import Solution
import solvers.graph.bfs as bfs
import solvers.graph.dijkstra as dijkstra
import solvers.knapsack.mitm as mitm
import solvers.knapsack.greedy as greedy

from sys import stdin, stdout
from plumbum import cli
from time import perf_counter
from collections import namedtuple


class SolverApplication(cli.Application):
    dijkstra_on = False
    bfs_on = False
    greedy_on = False
    mitm_on = False
    display_results = False
    problem_stream = stdin
    graph_retries = 1
    knapsack_retries = 1

    Result = namedtuple("Result", ["name", "time", "value"])

    @cli.switch(["-a", "--all"])
    def toggle_all(self):
        """Enable all algorithms"""
        self.greedy_on = True
        self.mitm_on = True
        self.bfs_on = True
        self.dijkstra_on = True

    @cli.switch(["-kg", "--greedy"])
    def toggle_greedy(self):
        """Enable greedy algorithm (approx. knapsack solver)"""
        self.greedy_on = True

    @cli.switch(["-km", "--mitm"])
    def toggle_mitm(self):
        """Enable Meet-In-The-Middle (MITM) algorithm (exact knapsack solver)"""
        self.mitm_on = True

    @cli.switch(["-gb", "--bfs"])
    def toggle_bfs(self):
        """Enable Breadth First Search algorithm (for graph)"""
        self.bfs_on = True

    @cli.switch(["-gd", "--dijkstra"])
    def toggle_dijkstra(self):
        """Enable Dijkstra algorithm (for graph)"""
        self.dijkstra_on = True

    @cli.switch(["-d", "--display"])
    def toggle_display(self):
        """Enables display of the results with matplotlib"""
        self.display_results = True

    @cli.switch("-f", str)
    def set_file(self, filepath):
        """Loads problem from file instead of stdin"""
        self.problem_stream = open(filepath)

    def bench(self, func, *args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        total_time = end - start

        return result, total_time

    def main(self):
        result_list = []
        graph_solutions = set()
        max_value = 0
        best_algo = None
        best_path = None
        best_set = None
        best_size = 0
        total_time_start = perf_counter()
        problem = problemparser.problem_from_input(self.problem_stream)
        if self.bfs_on:
            solver = bfs.BFS(problem)
            path, time = self.bench(solver.solve_graph)
            graph_solutions.add(tuple(path))
            r = self.Result("BFS", time, len(path))
            result_list.append(r)

        if self.dijkstra_on:
            solver = dijkstra.Dijkstra(problem)
            path, time = self.bench(solver.solve_graph)
            graph_solutions.add(tuple(path))
            value = len(path)
            r = self.Result("Dijkstra", time, value)
            result_list.append(r)

        if self.mitm_on:
            for path in graph_solutions:
                treasure_list = treasureparser.treasure_from_graph_with_path(problem.graph, path)
                treasures, time = self.bench(mitm.meet_in_the_middle, treasure_list, problem.trunk_size)
                total_value = 0
                total_size = 0
                for tr in treasures:
                    total_value += tr.value
                    total_size += tr.size
                r = self.Result("Mitm", time, total_value)
                result_list.append(r)
                if max_value < total_value:
                    max_value = total_value
                    best_algo = "MITM"
                    best_path = path
                    best_set = treasures
                    best_size = total_size

        if self.greedy_on:
            for path in graph_solutions:
                treasure_list = treasureparser.treasure_from_graph_with_path(problem.graph, path)
                treasures, time = self.bench(greedy.greedy, treasure_list, problem.trunk_size)
                total_value = 0
                total_size = 0
                for tr in treasures:
                    total_value += tr.value
                    total_size += tr.size
                r = self.Result("Greedy", time, total_value)
                result_list.append(r)
                if max_value < total_value:
                    max_value = total_value
                    best_algo = "Greedy"
                    best_path = path
                    best_set = treasures
                    best_size = total_size

        total_time_end = perf_counter()
        print(20*"=", "STATS", 21*"=")
        print("Name    | Time taken [s]| Score (path len/value)")
        for result in result_list:
            print("{:8}|{:>4.13f}|{:>23}".format(result.name, result.time, result.value))
        print(48*"=")
        print("Total time taken: {}s".format(total_time_end-total_time_start))
        print("Best path: {}".format(best_path))
        print("Best knapsack algorithm: {}".format(best_algo))
        print("Best set: {}".format(best_set))
        print("Total value: {}".format(max_value))
        print("Total size: {} out of max {}".format(best_size, problem.trunk_size))
        stdout.flush()
        if self.display_results:
            solution = Solution(problem, path=best_path, to_take=best_set)
            problemgui.draw_plot(solution)


if __name__ == "__main__":
    SolverApplication.run()
