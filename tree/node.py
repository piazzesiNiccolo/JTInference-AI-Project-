
from pgmpy.factors.discrete import DiscreteFactor
import numpy as np


class Clique(object):

    def __init__(self, nodes):
        self.name = '_'.join(node.variable for node in nodes)
        self.nodes = set(nodes)
        self.visited = False
        self.neighbors = set()
        self.init_table()

    def add_neighbor(self, neighbor, separator):
        n = (neighbor, separator)
        if (n not in self.neighbors) and (not self == neighbor):
            self.neighbors.add(n)
            neighbor.neighbors.add((self, separator))

    def init_table(self):
        self.table = DiscreteFactor([node.variable for node in self.nodes], 
                                    [node.variable_card for node in self.nodes], 
                                    np.ones(np.prod([node.variable_card for node in self.nodes])))
        for node in self.nodes:
            self.table *= node
        


class Separator(object):

    def __init__(self, clique1, clique2):
        self.nodes = clique1.nodes.intersection(clique2.nodes)
        self.neighbors = [clique1, clique2]
        self.init_table()
    
    def init_table(self):
        self.table = DiscreteFactor([node.variable for node in self.nodes],
                                    [node.variable_card for node in self.nodes],
                                    np.ones(np.prod([node.variable_card for node in self.nodes])))
        for node in self.nodes:
            self.table *= node
       
