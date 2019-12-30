from pybbn.graph.potential import PotentialUtil, Potential
from pybbn.graph.variable import Variable


class JTNode(object):
    # a node in a join tree is a clique made of nodes from the beliefs network

    def __init__(self, name, nodes):
        self.name = name
        self.variables = set(nodes)
        self.potential = PotentialUtil.get_potential_from_nodes(nodes)
        self.visited = False
        self.separators = set()

    def add_neighbor(self, neighbor, separator):
        ns = (neighbor, separator)
        if (ns not in self.separators) and (not self == neighbor):
            self.separators.add(ns)

    def init_potential(self, node):
        potential = Potential()
        potential *= node.potential


class Separator(object):
    def __init__(self, name, clique1, clique2):
        self.name = name
        self.variables = clique1.variables.intersection(clique2.variables)
        self.potential = PotentialUtil.get_potential_from_nodes(
            [clique1, clique2])
        self.visited = False
        self.neighbors = [clique1, clique2]


# class JoinTree(object):

    # def __init__(self, name, cliques):

    # def collectAndDistribute(self, root=none):
      #  self.set_root(root)
       # self.collect_evidence()
       # self.setVisited(false)
      #  self.distribute_evidence()
