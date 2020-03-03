import structures.adjacency_list as gal
import structures.adjacency_matrix as gam
import numpy

class IncidenceMatrix:
    def __init__(self):
        pass

    def load_matrix(self, file_path):
        self.matrix = numpy.loadtxt(file_path, int)

    def create_matrix(self, nr_of_vertices):
        self.matrix = numpy.empty((nr_of_vertices, 0), int)

    def __str__(self):
        return str(self.matrix)

    def to_string(self):
        return str(self.matrix)

    def add_edge(self, vertex_1, vertex_2):
        nr_of_vertices = len(self.matrix)
        self.matrix = numpy.c_[self.matrix, numpy.zeros(nr_of_vertices, int)] # adds column with zeros in it

        self.matrix[vertex_1][-1] = 1
        self.matrix[vertex_2][-1] = 1
        print(self.matrix)

    def get_neighbors(self, vertex):
        neighbors = numpy.where(self.matrix[vertex] == 1)
        return neighbors[0]

    def to_adjacency_matrix(self):
        pass

    def to_adjacency_list(self):
        pass