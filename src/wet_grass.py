print('importing modules...')
from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

##setup tables
r = TabularCPD("r",2,[[0.8],[0.2]],state_names={'r': ['no','yes']})
s = TabularCPD("s",2,[[0.9],[0.1]],state_names={'s': ['no','yes']})
w = TabularCPD('w',2,[[0.8,0],[0.2,1]],['r'],[2],state_names={'w': ['no','yes']})
h = TabularCPD('h', 2,[[1,0, 0.1, 0],[0,1 ,0.9, 1]],['s', 'r'], [2, 2],state_names={'h': ['no','yes']})
#setup tree
wr = Clique([w,r])
hrs = Clique([h,r,s])
jt = JunctionTree('f',[wr,hrs])
jt.add_separator(wr,hrs)

#run queries
print('\n\nQUERY SU H:\n')
##h query
print('p(h) senza evidenza')
print(jt.query('h'))
print('p(h) con evidenza r = yes')
r_evidence = ('r', 1)
print(jt.query('h',[r_evidence]))
jt.init_tree()
print('\np(h) con evidenza  w = yes e s = yes')
w_evidence = ('w',1)
s_evidence = ('s', 1)
print(jt.query('h',[w_evidence,s_evidence]))
print('\n\nQUERY SU W:\n')
##w query
jt.init_tree()
print('p(w) senza evidenza')
print(jt.query('w'))
print('p(w) con evidenza s = yes e h = no')
s_evidence = ('s', 1)
h_evidence = ('h',0)
print(jt.query('w',[s_evidence,h_evidence]))
print('\n\nQUERY SU R:\n')
#r query
jt.init_tree()
print('p(r) senza evidenza')
print(jt.query('r'))
print('p(r) con evidenza  w = yes')
w_evidence = ('w',1)
print(jt.query('r',[w_evidence]))
jt.init_tree()
print('p(r) con evidenza  w = yes e h = yes')
h_evidence = ('h', 1)
print(jt.query('r',[w_evidence,h_evidence]))

print('\n\nQUERY SU S:\n')
#s query
jt.init_tree()
print('p(s) senza evidenza')
print(jt.query('s'))
print('p(s) con evidenza  w = yes e h = yes')
w_evidence = ('w',1)
h_evidence = ('h', 1)
print(jt.query('s',[w_evidence,h_evidence]))

