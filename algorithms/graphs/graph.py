"""
Graphs Module
"""


class Vertex:
    def __init__(self, key):
        self.id = key
        # map from a neighbour vertex to the weight of the edge
        self.connected_to = {}

    def __str__(self):
        return str(self.id) + " connected to: " + str([x.id for x in self.connected_to])

    def add_neighbour(self, neighbour, weight):
        """
        Adds the neighbour to the connected_to map with the corresponding weight.
        :param neighbour: the neighbour to be added
        :param weight: the weight of the edge
        """
        self.connected_to[neighbour] = weight

    def get_connections(self):
        """
        :return: all neighbours of this vertex
        """
        return self.connected_to.keys()

    def get_id(self):
        """
        :return: the id of this vertex
        """
        return self.id

    def get_weight(self, neighbour):
        """
        Returns the weight of the edge between this vertex and neighbour
        :param neighbour: the neighbour
        :return: the weight of the edge
        """
        return self.connected_to[neighbour]


class Graph:
    def __init__(self, directed=True):
        self.vertices = {}
        self.num_vertices = 0
        self.directed = directed

    def __contains__(self, item):
        return item in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def connected(self, key_1, key_2):
        """
        :param key_1: vertex with key_1
        :param key_2: vertex with key_2
        :return: true if vertex 1 is connected to vertex 2, false otherwise
        """
        neighbours = self.vertices[key_1].get_connections()
        for neighbour in neighbours:
            if key_2 == neighbour.get_id():
                return True
        return False

    def get_vertex(self, key):
        """
        :param key: key of the vertex
        :return: the Vertex object given the key, or raises KeyError
        """
        if key in self.vertices:
            return self.vertices[key]
        else:
            raise KeyError("No Vertex with that key.")

    def get_vertices(self):
        """
        :return: the keys of the vertices in the graph
        """
        return self.vertices.keys()

    def add_vertex(self, key):
        """
        Adds a vertex with the specified key to the graph.
        :param key: the key of the vertex
        """
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

    def add_edges(self, edges: list):
        """
        Calls self.add_edges for all edges in the edges list.
        :param edges: list of edges
        """
        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, *edge):
        """
        Adds an edge given a tuple of the form:
         - (vertex_1, vertex_2) for non-weighted graphs
         - (vertex_1, vertex_2, weight) for weighted graphs
        where vertex_1 and vertex_2 are keys, not Vertex objects.
        :param edge: the edge to be added
        """
        vertex_1, vertex_2, *cost = edge
        if vertex_1 not in self.vertices:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.vertices:
            self.add_vertex(vertex_2)
        if len(cost) == 0:
            self.vertices[vertex_1].add_neighbour(self.vertices[vertex_2], 0)
            if not self.directed:
                self.vertices[vertex_2].add_neighbour(self.vertices[vertex_1], 0)
        else:
            self.vertices[vertex_1].add_neighbour(self.vertices[vertex_2], cost[0])
            if not self.directed:
                self.vertices[vertex_2].add_neighbour(self.vertices[vertex_1], cost[0])


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
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
            print("({}, {}) with weight {}".format(v.get_id(), w.get_id(), v.get_weight(w)))
    print(g.connected(0, 1))
