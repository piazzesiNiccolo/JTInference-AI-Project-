
from bayes import Clique,Separator
from JoinTree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD,DiscreteFactor
import numpy as np

##WET GRASS
r = TabularCPD("r",2,[[0.8],[0.2]])
s = TabularCPD("s",2,[[0.9],[0.1]])
w = TabularCPD('w',2,[[0.8,0],[0.2,1]],['r'],[2])
h = TabularCPD('h', 2,[[1,0.1,0,0],[0,0.9,1,1]],['r', 's'], [2, 2])
wr = Clique([w,r])
hrs = Clique([h,r,s])
print(hrs.cpt.marginalize(['r','h'],False))
jt = JunctionTree('f',wr,[wr,hrs])
jt.add_separator(wr,hrs)
jt.enter_evidence('h',1)
jt.enter_evidence('w',1)

##TO DO: scelta root,riguardare aggiunta vicini,e struttura generale
print(hrs.cpt.marginalize(['r','h'],False))


##ICY ROAD

icy = TabularCPD('i',2,[[0.3],[0.7]])
holmes = TabularCPD('h',2,[[0.9,0.2],[0.1,0.8]],['i'],[2])
watson = TabularCPD('w',2,[[0.9,0.2],[0.1,0.8]],['i'],[2])
print(icy)
print(holmes)
print(watson)

iw = Clique([icy,watson])
ih = Clique([icy,holmes])

jt2 = JunctionTree('t',iw,[iw,ih])
jt2.add_separator(iw,ih)
jt2.enter_evidence('w',0)
print(ih.cpt.marginalize(['h'],False))
print(iw.cpt.marginalize(['w'],False))