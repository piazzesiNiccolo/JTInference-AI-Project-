
from pgmpy.factors.discrete import DiscreteFactor
import numpy as np



class Clique(object):
    
    def __init__(self, nodes):
        self.name = ''.join(node.variable for node in nodes)
        self.nodes = set(nodes)
        self.visited = False
        self.neighbors = set()
        self.cpt = self.init_cpt()
        

    def add_neighbor(self, neighbor,separator):
        n = (neighbor,separator)
        if (n not in self.neighbors) and (not self == neighbor):
            self.neighbors.add(n)
            neighbor.neighbors.add((self,separator))
    
    def init_cpt(self):
        cpt = DiscreteFactor([node.variable for node in self.nodes],[2 for i in range(len(self.nodes))],np.ones(2**len(self.nodes)))
        for node in self.nodes:
            cpt.product(node)
        cpt.normalize()
        return cpt

class Separator(object):
    
    def __init__(self,clique1,clique2):
        self.nodes = clique1.nodes.intersection(clique2.nodes)
        self.visited = False
        self.cpt = self.init_cpt()
        self.neighbors = [clique1,clique2]

    def init_cpt(self):
        cpt = DiscreteFactor([node.variable for node in self.nodes],[2 for i in range(len(self.nodes))],np.ones(2**len(self.nodes)))
        for node in self.nodes:
            cpt.product(node)
            cpt.normalize()
        return cpt