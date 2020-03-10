from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

##setup tables
visit_to_asia = TabularCPD('a',2,[[0.99],[0.01]])
smoker = TabularCPD('s',2,[[0.5], [0.5]])
tubercolosis = TabularCPD('t', 2, [[0.99, 0.95], [0.01, 0.05]],['a'],[2])
lung_cancer =  TabularCPD('l', 2, [[0.99, 0.9], [0.01, 0.1]],['s'],[2])
bronchitis =  TabularCPD('b', 2, [[0.7, 0.4], [0.3, 0.6]],['s'],[2])
tubercolosis_or_cancer =  TabularCPD('e', 2, [[1, 0, 0, 0], [0, 1, 1, 1]],['t', 'l'],[2, 2])
positive_xray =  TabularCPD('x', 2, [[0.95, 0.02], [0.05, 0.98]],['e'],[2])
dyspnoea =  TabularCPD('d', 2, [[0.9, 0.3, 0.2, 0.1], [0.1, 0.7, 0.8, 0.9]],['b','e'],[2, 2])
#setup tree
ebs = Clique([tubercolosis_or_cancer,bronchitis, smoker])
esl = Clique([tubercolosis_or_cancer, smoker, lung_cancer])
ebd = Clique([tubercolosis_or_cancer, bronchitis, dyspnoea])
elt = Clique([tubercolosis_or_cancer,lung_cancer,tubercolosis])
ex = Clique([tubercolosis_or_cancer,positive_xray])
ta = Clique([tubercolosis,visit_to_asia])
tree = JunctionTree('chest_tree',[ebs,esl,ebd,elt,ex,ta])
tree.add_separator(ebs,esl)
tree.add_separator(ebs,ebd)
tree.add_separator(esl,elt)
tree.add_separator(ebd,ex)
tree.add_separator(elt, ta)
print(ta.table.marginalize(['t'],False))

#run queries
print('\n\nQUERY SU VISIT_TO_ASIA\n')
print('p(asia) senza evidenza')
print(tree.query('a'))
e_evidence = ('e', 1)
t_evidence =('t', 1)
print('p(asia) con evidenza e = yes e t = yes')
print(tree.query('a',[e_evidence,t_evidence]))
