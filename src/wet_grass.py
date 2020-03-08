from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

##WET GRASS
r = TabularCPD("r",2,[[0.8],[0.2]])
s = TabularCPD("s",2,[[0.9],[0.1]])
w = TabularCPD('w',2,[[0.8,0],[0.2,1]],['r'],[2])
h = TabularCPD('h', 2,[[1,0.1,0,0],[0,0.9,1,1]],['r', 's'], [2, 2])
wr = Clique([w,r])
hrs = Clique([h,r,s])
print(hrs.table.marginalize(['r','h'],False))
jt = JunctionTree('f',[wr,hrs])
jt.add_separator(wr,hrs)
jt.enter_evidence('h',0,2)



print(hrs.table.marginalize(['r','h'],False))