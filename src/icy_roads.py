from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

##ICY ROADS
icy = TabularCPD('i',2,[[0.3],[0.7]])
holmes = TabularCPD('h',2,[[0.9,0.2],[0.1,0.8]],['i'],[2])
watson = TabularCPD('w',2,[[0.9,0.2],[0.1,0.8]],['i'],[2])
print(watson.marginalize(['i'],False))
iw = Clique([icy,watson])
ih = Clique([icy,holmes])

jt2 = JunctionTree('t',[iw,ih])
jt2.add_separator(iw,ih)
jt2.propagate()
jt2.enter_evidence('h',1,holmes.variable_card)
jt2.enter_evidence('i',0,icy.variable_card)
print(iw.table.marginalize(['i'],False))
