from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

fire = TabularCPD('f',2,[[0.99],[0.01]])
tampering = TabularCPD('t',2,[[0.98], [0.02]])
smoke = TabularCPD('s',2 ,[[0.99, 0.1], [0.01,0.9]],['f'],[2])
alarm = TabularCPD('a',2 ,[[0.9999, 0.15, 0.01, 0.5], [0.0001,0.85,0.99, 0.5]],['f','t'],[2,2])
leaving = TabularCPD('l',2 ,[[0.999, 0.12], [0.001,0.88]],['a'],[2])
report = TabularCPD('r',2 ,[[0.99, 0.25], [0.01,0.75]],['l'],[2])
la = Clique([leaving,alarm])
aft = Clique([alarm,fire,tampering])
lr = Clique([leaving,report])
fs = Clique([fire,smoke])
print(fs.table.marginalize(['s'],False))

tree = JunctionTree('fire_tree',[la,aft,lr,fs])
tree.add_separator(la,aft)
tree.add_separator(la,lr)
tree.add_separator(aft,fs)
tree.enter_evidence('r',1,2)
print(fs.table.marginalize(['s'],False))
