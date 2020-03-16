print('importing modules...')
from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

##setup tables
rain = TabularCPD("r",2,[[0.9],[0.1]],state_names={'r': ['no','yes']})
sprinkler  = TabularCPD("s",2,[[0.9],[0.1]],state_names={'s': ['no','yes']})
watson = TabularCPD('w',2,[[0.9,0.01],[0.1,0.99]],['r'],[2],state_names={'w': ['no','yes']})
holmes = TabularCPD('h', 2,[[1,0.01, 0.1, 0],[0,0.99 ,0.9, 1]],['s', 'r'], [2, 2],state_names={'h': ['no','yes']})
gibbon = TabularCPD('g',2,[[0.9,0.01],[0.1,0.99]],['r'],[2],state_names={'g': ['no','yes']})

#setup tree
rg = Clique([rain,gibbon])
rhs = Clique([rain,holmes,sprinkler])
rw = Clique([rain,watson])
jt = JunctionTree('tree',[rg,rhs,rw],rg)
jt.add_separator(rg,rhs)
jt.add_separator(rg,rw)

#run queries
print('\n\nQUERY SU HOLMES:\n')
##h query
print('p(h) senza evidenza')
print(jt.query('h'))
print('\np(h) con evidenza  w = yes e s = yes')
w_evidence = ('w',1)
s_evidence = ('s', 1)
print(jt.query('h',[w_evidence,s_evidence]))

print('\n\nQUERY SU WATSON:\n')
jt.init_tree()
print('p(w) senza evidenza')
print(jt.query('w'))
print('p(w) con evidenza g = yes e h = no')
g_evidence = ('g', 1)
h_evidence = ('h',0)
print(jt.query('w',[g_evidence,h_evidence]))

print('\n\nQUERY SU RAIN:\n')
#r query
jt.init_tree()
print('p(r) senza evidenza')
print(jt.query('r'))
print('p(r) con evidenza  w = yes e h = yes')
h_evidence = ('h', 1)
print(jt.query('r',[w_evidence,h_evidence]))

print('\n\nQUERY SU SPRNKLER:\n')
#s query
jt.init_tree()
print('p(s) senza evidenza')
print(jt.query('s'))
print('p(s) con evidenza  h = yes')
print(jt.query('s',[h_evidence]))

print('\n\nQUERY SU GIBBON:\n')
jt.init_tree()
print('p(gibbon) senza evidenza')
print(jt.query('g'))
print('p(g) con evidenza  w = yes')
w_evidence = ('w', 1)
print(jt.query('g',[w_evidence]))

