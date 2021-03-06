class Vertex:

    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=0):
        if neighbor not in self.neighbors:
            self.neighbors[neighbor] = weight

    def __str__(self):
        return '{} Neighbors {}'.format(
            self.key,
            [x for x in self.neighbors]
        )

    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    def get_vertex(self, key):
        try:
            return self.vertices[key]
        except KeyError:
            return None

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, from_key, to_key, weight):
        if from_key not in self.vertices:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.vertices:
            self.add_vertex(Vertex(to_key))
        self.vertices[from_key].add_neighbor(self.vertices[to_key], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())


g = Graph()
for i in range(6):
    g.add_vertex(Vertex(i))

g.add_edge(0, 1, 5)
g.add_edge(0, 5, 2)
g.add_edge(1, 2, 4)
g.add_edge(2, 3, 9)
g.add_edge(3, 4, 7)
g.add_edge(3, 5, 3)
g.add_edge(4, 0, 1)
g.add_edge(5, 4, 8)
g.add_edge(5, 2, 1)

for v in g:
    for w in v.get_connections():
        print('{} -> {}'.format(v.key, w.key))


"""
You can also use a dictionary to achieve the same structure:

{
    0: {1: 5, 5: 2},
    1: {2: 4},
    2: {3: 9},
    3: {4: 7, 5: 3},
    4: {0: 1},
    5: {4: 8}
}
"""


