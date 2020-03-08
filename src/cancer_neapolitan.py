from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD


#cancer_neapolitan
print('creating network...')
Metastatic_Cancer = TabularCPD('m',2,[[0.8],[0.2]])
Serum_Calcium = TabularCPD('s',2,[[0.8,0.2],[0.2,0.8]],['m'],[2])
Brain_Tumor =  TabularCPD('b',2,[[0.95,0.8],[0.05,0.2]],['m'],[2])
Coma =  TabularCPD('c', 2,[[0.95,0.1,0.3,0.2],[0.05,0.9,0.7,0.8]],['b','s'], [2, 2])
print(Coma.marginalize(['b','s'],False))
Severe_Headache = TabularCPD('h', 2,[[0.4,0.2,],[0.6,0.8]],['b'], [2])

print('setting up junction tree...')
bsm = Clique([Metastatic_Cancer,Serum_Calcium,Brain_Tumor])
sbc = Clique([Serum_Calcium,Brain_Tumor,Coma])
bh = Clique([Brain_Tumor,Severe_Headache])
jt = JunctionTree('tree',[bsm,sbc,bh])
jt.add_separator(bsm,sbc)
jt.add_separator(bsm,bh)
jt.enter_evidence('c',1,Coma.variable_card)
print(bh.table.marginalize([x for x in bh.table.scope() if x != 'h'],False))


