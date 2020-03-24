
from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD


#cancer_neapolitan
def cancer_neapolitan_example():
    
    print('RUNNING CANCER NEAPOLITAN EXAMPLE\n\n')
    print('setting up network...')
    Metastatic_Cancer = TabularCPD('m',2,[[0.8],[0.2]])
    Serum_Calcium = TabularCPD('s',2,[[0.8,0.2],[0.2,0.8]],['m'],[2])
    Brain_Tumor =  TabularCPD('b',2,[[0.95,0.8],[0.05,0.2]],['m'],[2])
    Coma =  TabularCPD('c', 2,[[0.95,0.1,0.3,0.2],[0.05,0.9,0.7,0.8]],['b','s'], [2, 2])
    Severe_Headache = TabularCPD('h', 2,[[0.4,0.2,],[0.6,0.8]],['b'], [2])
    print('setting up junction tree...')
    bsm = Clique([Metastatic_Cancer,Serum_Calcium,Brain_Tumor])
    sbc = Clique([Serum_Calcium,Brain_Tumor,Coma])
    bh = Clique([Brain_Tumor,Severe_Headache])
    jt = JunctionTree('tree',[bsm,sbc,bh])
    jt.add_separator(bsm,sbc)
    jt.add_separator(bsm,bh)

    print('\n\n QUERY SU METASTATIC CANCER\n')
    print('p(m_cancer) senza evidenza: ')
    print(jt.query('m'))
    print('p(m_cancer con evidenza brain_tumor = 1 e coma = 1')
    b_evidence = ('b',1)
    c_evidence = ('c',1)
    print(jt.query('m',[b_evidence,c_evidence]))
    
    input('\n PRESS ANY KEY TO RUN NEXT QUERY')
    jt.init_tree()
    print('\n\n QUERY SU SERUM CALCIUM\n')
    print('p(s_calcium) senza evidenza: ')
    print(jt.query('s'))
    print('p(s_calcium) con evidenza metastatic_cancer = 0')
    m_evidence = ('m',0)
    print(jt.query('s',[m_evidence]))

    input('\n PRESS ANY KEY TO RUN NEXT QUERY')
    jt.init_tree()
    print('\n\n QUERY SU BRAIN TUMOR\n')
    print('p(b_tumor) senza evidenza: ')
    print(jt.query('b'))
    print('p(b_tumor) con evidenza metastatic_cancer = 0, serum_calcium = 1 e severe_headaches = 1')
    s_evidence = ('s', 1)
    h_evidence = ('h', 1)
    print(jt.query('b',[m_evidence,s_evidence,h_evidence]))

    input('\n PRESS ANY KEY TO RUN NEXT QUERY')
    jt.init_tree()
    print('\n\n QUERY SU COMA\n')
    print('p(coma) senza evidenza: ')
    print(jt.query('c'))
    print('p(coma) con evidenza brain tumor = 1 e severe_headaches = 1 ')
    print(jt.query('c',[b_evidence, h_evidence]))

    input('\n PRESS ANY KEY TO RUN NEXT QUERY')
    jt.init_tree()
    print('\n\n QUERY SU SEVERE_HEADACHES\n')
    print('p(headaches) senza evidenza: ')
    print(jt.query('h'))
    print('p(headaches) con evidenza brain tumor = 1 e metastatic_cancer = 0 ')
    print(jt.query('h',[b_evidence, m_evidence]))









