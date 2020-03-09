print('importing modules...')
from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

##WET GRASS
r = TabularCPD("r",2,[[0.8],[0.2]],state_names={'r': ['no','yes']})
s = TabularCPD("s",2,[[0.9],[0.1]],state_names={'s': ['no','yes']})
w = TabularCPD('w',2,[[0.8,0],[0.2,1]],['r'],[2],state_names={'w': ['no','yes']})
h = TabularCPD('h', 2,[[1,0.1,0,0],[0,0.9,1,1]],['r', 's'], [2, 2],state_names={'h': ['no','yes']})
wr = Clique([w,r])
hrs = Clique([h,r,s])
print('p(h) senza evidenza')
jt = JunctionTree('f',[wr,hrs])
jt.add_separator(wr,hrs)
print(jt.query('h'))
print('p(h) con evidenza r = yes')
r_evidence = ('r', 1)
print(jt.query('h',[r_evidence]))

input('proseguire col prossimo esempio?')
jt.init_tree()
print('p(w) senza evidenza')
print(jt.query('w'))
print('p(w) con evidenza s = yes e r = no')
s_evidence = ('s', 1)
h_evidence = ('h',0)
print(jt.query('w',[s_evidence,h_evidence]))

