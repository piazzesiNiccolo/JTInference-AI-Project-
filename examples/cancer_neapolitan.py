
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

    print('\n\nMETASTATIC CANCER\n')
    print('p(m_cancer): ')
    print(jt.query('m'))
    print('p(m_cancer | brain_tumor = 1, coma = 1)')
    b_evidence = (Brain_Tumor,1)
    c_evidence = (Coma,1)
    print(jt.query('m',[b_evidence,c_evidence]))
    
    input('\n PRESS ENTER TO RUN NEXT QUERY')
    jt.init_tree()
    print('\n\nSERUM CALCIUM\n')
    print('p(s_calcium): ')
    print(jt.query('s'))
    print('p(s_calcium | metastatic_cancer = 0)')
    m_evidence = (Metastatic_Cancer,0)
    print(jt.query('s',[m_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    jt.init_tree()
    print('\n\nBRAIN TUMOR QUERY\n')
    print('p(b_tumor): ')
    print(jt.query('b'))
    print('p(b_tumor | metastatic_cancer = 0, serum_calcium = 1, severe_headaches = 1)')
    s_evidence = (Serum_Calcium, 1)
    h_evidence = (Severe_Headache, 1)
    print(jt.query('b',[m_evidence,s_evidence,h_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    jt.init_tree()
    print('\n\nCOMA\n')
    print('p(coma): ')
    print(jt.query('c'))
    print('p(coma | brain tumor = 1, severe_headaches = 1) ')
    print(jt.query('c',[b_evidence, h_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    jt.init_tree()
    print('\n\nSEVERE_HEADACHES\n')
    print('p(headaches): ')
    print(jt.query('h'))
    print('p(headaches | brain tumor = 1, metastatic_cancer = 0 )')
    print(jt.query('h',[b_evidence, m_evidence]))









