
from bayes import Clique,Separator
from JoinTree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD,DiscreteFactor
import numpy as np

r = TabularCPD("r",2,[[0.8],[0.2]])
s = TabularCPD("s",2,[[0.9],[0.1]])
w = TabularCPD('w',2,[[0.8,0],[0.2,1]],['r'],[2])
h = TabularCPD('h', 2,[[1,0.1,0,0],[0,0.9,1,1]],['r', 's'], [2, 2])
print(r)
print(s)
print(w)
print(h)
ff = TabularCPD('h',2,[[0],[1]])
ff2 = TabularCPD('w',2,[[0],[1]])
print(ff)
wr = Clique([w,r])
hrs = Clique([h,r,s])
wr.init_cpt()
hrs.init_cpt()
print(hrs.cpt.marginalize(['r','h'],False))
jt = JunctionTree('f',wr,[wr,hrs])
jt.add_separator(wr,hrs)
jt.enter_evidence('h',1)
jt.enter_evidence('w',1)

##TO DO: scelta root,riguardare aggiunta vicini,e struttura generale
print(hrs.cpt.marginalize(['r','h'],False))


