import numpy as np
import copy
from bayes import Clique, Separator
from pgmpy.factors.discrete.CPD import TabularCPD


class JunctionTree(object):

    def __init__(self, name, root, list_cliques, separators=set()):
        self.name = name
        self.cliques = set(list_cliques)
        self.separators = separators
        self.root = root
        self.initialize = False

    def add_separator(self, clique1, clique2):
        sep = Separator(clique1, clique2)
        sep.init_cpt()
        self.separators.add(sep)
        clique1.add_neighbor(clique2, sep)

    def enter_evidence(self, variable, value):
        ev = TabularCPD(variable, 2, [[0], [0]])
        ev.get_values()[value] = 1
        for clique in self.cliques:
            if next((x for x in clique.nodes if x.variable == variable)):
                clique.cpt.product(ev)
                break
        self.propagate()

    def propagate(self):
        self.set_visited()
        self.collect(None, self.root, None, True)
        self.set_visited()
        self.distribute(self.root)
        for cl in self.cliques:
            cl.cpt.normalize()
        for sep in self.separators:
            sep.cpt.normalize()

    def collect(self, pc, cc, sepset, send):
        cc.cpt.normalize()
        print('collect')
        cc.visited = True
        for neighbor, sep in cc.neighbors:
            if not neighbor.visited:
                self.collect(cc, neighbor, sep, False)
        if not send:
            self.pass_message(cc, pc, sepset)

    def distribute(self, clique):
        clique.cpt.normalize()
        print('distribute')
        clique.visited = True
        for neighbor, sep in clique.neighbors:
            if not neighbor.visited:
                self.pass_message(clique, neighbor, sep)
                self.distribute(neighbor)

    def pass_message(self, from_clique: Clique, to_clique: Clique, sep: Separator):
        x = [node.variable for node in from_clique.nodes.difference(sep.nodes)]
        new = from_clique.cpt.marginalize(x, False)
        to_clique.cpt.product(new)
        to_clique.cpt.divide(sep.cpt)
        sep.cpt = new

    def set_visited(self, visit=False):
        for c in self.cliques:
            c.visited = visit
