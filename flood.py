from node import Clique,Separator
from junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

rain = TabularCPD('r', 2, [[0.99], [0.01]])
burglary = TabularCPD('b', 2, [[0.5], [0.5]])
earthquake = TabularCPD('e', 2, [[0.9], [0.1]])
flood = TabularCPD('f', 2, [[1, 0.9], [0, 0.1]], ['r'], [2])
seismometer = TabularCPD('s', 3, [[0.97,0.01,0.01,0], [0.02,0.97,0.02,0.03],[0.01,0.02,0.97,0.97]], ['b','e'], [2, 2])  
alarm = TabularCPD('a' ,[[0.99,0.01,0.01,0, 0.01, 0, 0, 0],[0.01, 0.99 ,0.99, 1 ,0.99, 1, 1, 1]],['e','b','f'], [2, 2, 2])


feba = Clique([flood,earthquake,burglary,alarm])
ebs = Clique([earthquake,burglary,seismometer])
fr = Clique([flood,rain])

tree = JunctionTree('flood_tree',[feba,ebs,fr])
tree.add_separator(feba, ebs)
tree.add_separator(feba,fr)
feba.table