
from node import Clique, Separator
import numpy as np
import random
from pgmpy.factors.discrete.CPD import TabularCPD
np.seterr(divide='ignore', invalid='ignore')

class JunctionTree(object):

    def __init__(self, name,  list_cliques,root = None, separators=set()):
        self.name = name
        self.cliques = set(list_cliques)
        self.separators = separators
        self.root = root if root else random.choice(list(self.cliques))

    def set_root(self,root):
        self.root = root
    
    def add_separator(self, clique1, clique2):
        sep = Separator(clique1, clique2)
        self.separators.add(sep)
        clique1.add_neighbor(clique2, sep)

    def enter_evidence(self, variable, value, cardinality):
        ev = TabularCPD(variable, 2, [[0] for i in range(cardinality)])
        ev.get_values()[value] = 1
        for clique in self.cliques:
            found = False
            for node in clique.nodes:
                if node.variable == variable:
                    clique.table.product(ev)
                    found = True
                    break
                if found:
                    break
        self.propagate()

    def propagate(self):
        self.set_visited(False)
        self.collect_evidence(None, self.root, None, True)
        self.set_visited(False)
        self.distribute_evidence(self.root)
        
        for cl in self.cliques:
            cl.table.normalize()
        for sep in self.separators:
            sep.table.normalize()

    def collect_evidence(self, pc, cc, sepset, send):
        cc.table.normalize()
        cc.visited = True
        for neighbor, sep in cc.neighbors:
            if not neighbor.visited:
                self.collect_evidence(cc, neighbor, sep, False)
        if not send:
            self.pass_message(cc, pc, sepset)

    def distribute_evidence(self, clique):
        clique.table.normalize()
        clique.visited = True
        for neighbor, sep in clique.neighbors:
            if not neighbor.visited:
                self.pass_message(clique, neighbor, sep)
                self.distribute_evidence(neighbor)

    def pass_message(self, from_clique: Clique, to_clique: Clique, sep: Separator):
        x = [node.variable for node in from_clique.nodes.difference(sep.nodes)]
        new = from_clique.table.marginalize(x, False)
        to_clique.table.product(new)
        to_clique.table.divide(sep.table)
        sep.table = new

    def set_visited(self, visit=True):
        for c in self.cliques:
            c.visited = visit
