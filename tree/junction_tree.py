
from tree.node import Clique, Separator
import numpy as np
import random
import copy
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

    def init_tree(self):
        
        for cl in self.cliques:
            cl.init_table()
        for sep in self.separators:
            sep.init_table()
    
    
    def normalize(self):
        
        for cl in self.cliques:
            cl.table.normalize()
        for sep in self.separators:
            sep.table.normalize()

    def is_visited(self, visit=True):
        for c in self.cliques:
            c.visited = visit
    
    def query(self,variable,evidence_list = []):
        
        for var,value in evidence_list:
            self.enter_evidence(var,value)
        self.propagate()
        for clique in self.cliques:
            for node  in clique.nodes:
                if node.variable == variable:
                    return clique.table.marginalize([x for x in clique.table.scope() if x != variable],False)
    
    def enter_evidence(self, node, value):
        ev = TabularCPD(node.variable,node.variable_card, [[0] for i in range(node.variable_card)])
        ev.get_values()[value] = 1
        for clique in self.cliques:
            if ev.variable in clique.table.scope():
                clique.table *= ev
                break
        
    
    def propagate(self):
        
        self.is_visited(False)
        print('collecting evidence...')
        self.collect_evidence(None, self.root, None, True)
        self.is_visited(False)
        print('distributing evidence...')
        self.distribute_evidence(self.root)
        self.normalize()
        

    def collect_evidence(self, pc, cc, sepset, is_root):
        cc.visited = True
        for neighbor, sep in cc.neighbors:
            if not neighbor.visited:
                self.collect_evidence(cc, neighbor, sep, False)
        if not is_root:
            self.pass_message(cc, pc, sepset)

    def distribute_evidence(self, clique):
        clique.visited = True
        for neighbor, sep in clique.neighbors:
            if not neighbor.visited:
                self.pass_message(clique, neighbor, sep)
                self.distribute_evidence(neighbor)

    def pass_message(self, from_clique: Clique, to_clique: Clique, sep: Separator):
        
        x = [node.variable for node in from_clique.nodes.difference(sep.nodes)]
        new = from_clique.table.marginalize(x, False)
        to_clique.table *= new
        to_clique.table /= sep.table
        sep.table = new

    
