import os
from collections import defaultdict, deque


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        if self.distances.get((from_node, to_node)) is None or distance < self.distances.get((from_node, to_node)):
            self.edges[from_node].append(to_node)
            self.edges[to_node].append(from_node)
            self.distances[(from_node, to_node)] = distance
        else:
            pass


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)


def write_file(case, result):
    outfile.write("Case #" + str(case + 1) + ": " + str(result) + "\n")


in_file_path = os.path.join(os.path.dirname(__file__), "testInput.txt")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())
        steps = []
        for case in range(cases):
            case_data = list(map(int, (infile.readline().split())))
            floors = case_data[0]
            num_shortcuts = case_data[1]
            tower = Graph()
            normal_weight = 0
            start_v = 1
            tower.add_node(start_v)
            goal_v = 0

            for vertex in range(floors):
                if vertex != floors - 1:
                    normal_weight += vertex + 1
                if vertex == floors - 1:
                    goal_v = vertex + 1
                    tower.add_node(goal_v)
            for i, options in enumerate(range(num_shortcuts)):
                shortcut = list(map(int, (infile.readline()).split()))
                tower.add_node(shortcut[0])
                tower.add_node(shortcut[1])
                tower.add_edge(shortcut[0], shortcut[1], shortcut[2])
                tower.add_edge(shortcut[1], shortcut[0], 0)  # camino de vuelta
                if i == 0:
                    distance = 0
                    for i in range(shortcut[0]):
                        distance += i
                    tower.add_edge(start_v, shortcut[0], distance)
                elif i == num_shortcuts - 1:
                    tower.add_edge(shortcut[1], goal_v, shortcut[1])
                if shortcut[0] - 1 in tower.nodes:
                    tower.add_edge(shortcut[0] - 1, shortcut[0],
                                   shortcut[0] - 1)
                    tower.add_edge(shortcut[0], shortcut[0] - 1, 0)

            tower.add_edge(start_v, goal_v, normal_weight)
            tower.add_edge(goal_v, start_v, 0)  # camino de vuelta
            print("NODOS: ", tower.nodes)
            print("GRAFO: ", tower.distances)
            if floors == 1:
                write_file(case, 0)
            else:
                print("DIJSKTRA", shortest_path(tower, 1, floors))
                visited, path = shortest_path(tower, 1, floors)
                write_file(case, visited)
