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
