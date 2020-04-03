
from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD


#cancer_neapolitan
def cancer_neapolitan_example():
    
    print('RUNNING CANCER NEAPOLITAN EXAMPLE\n\n')
    print('setting up network...')
    Metastatic_Cancer = TabularCPD('metastatic_cancer',2,[[0.8],[0.2]],state_names={'metastatic_cancer':['no','yes']})
    
    Serum_Calcium = TabularCPD('serum_calcium',2,[[0.8,0.2],[0.2,0.8]],['metastatic_cancer'],[2],
                                    state_names={'serum_calcium':['no','yes'],'metastatic_cancer':['no','yes']})
    
    Brain_Tumor =  TabularCPD('brain_tumor',2,[[0.95,0.8],[0.05,0.2]],['metastatic_cancer'],[2],
                                    state_names={'brain_tumor':['no','yes'],'metastatic_cancer':['no','yes']})
   
    Coma =  TabularCPD('coma', 2,[[0.95,0.1,0.3,0.2],[0.05,0.9,0.7,0.8]],['brain_tumor','serum_calcium'], [2, 2],
                            state_names={'coma':['no','yes'],'brain_tumor':['no','yes'],'serum_calcium':['no','yes']})
    
    Severe_Headache = TabularCPD('severe_headaches', 2,[[0.4,0.2,],[0.6,0.8]],['brain_tumor'], [2],
                                        state_names={'severe_headaches':['no','yes'],'brain_tumor':['no','yes']})
    
    print('setting up junction tree...')
    bsm = Clique([Metastatic_Cancer,Serum_Calcium,Brain_Tumor])
    sbc = Clique([Serum_Calcium,Brain_Tumor,Coma])
    bh = Clique([Brain_Tumor,Severe_Headache])
    
    jt = JunctionTree('tree',[bsm,sbc,bh])
    jt.add_separator(bsm,sbc)
    jt.add_separator(bsm,bh)

    print('\n\nMETASTATIC CANCER\n')
    print('p(metastatic_cancer): ')
    print(jt.query('metastatic_cancer'))
    print('p(metastatic_cancer | brain_tumor = yes, coma = yes)')
    b_evidence = (Brain_Tumor,1)
    c_evidence = (Coma,1)
    print(jt.query('metastatic_cancer',[b_evidence,c_evidence]))
    
    input('\n PRESS ENTER TO RUN NEXT QUERY')
    jt.init_tree()
    print('\n\nSERUM CALCIUM\n')
    print('p(serum_calcium): ')
    print(jt.query('serum_calcium'))
    print('p(serum_calcium | metastatic_cancer = no)')
    m_evidence = (Metastatic_Cancer,0)
    print(jt.query('serum_calcium',[m_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    jt.init_tree()
    print('\n\nBRAIN TUMOR QUERY\n')
    print('p(brain_tumor): ')
    print(jt.query('brain_tumor'))
    print('p(brain_tumor | metastatic_cancer = no, serum_calcium = yes, severe_headaches = no)')
    s_evidence = (Serum_Calcium, 1)
    h_evidence = (Severe_Headache, 1)
    print(jt.query('brain_tumor',[m_evidence,s_evidence,h_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    jt.init_tree()
    print('\n\nCOMA\n')
    print('p(coma): ')
    print(jt.query('coma'))
    print('p(coma | brain_tumor = yes, severe_headaches = yes) ')
    print(jt.query('coma',[b_evidence, h_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    jt.init_tree()
    print('\n\nSEVERE_HEADACHES\n')
    print('p(severe_headaches): ')
    print(jt.query('severe_headaches'))
    print('p(severe_headaches | brain_tumor = yes, metastatic_cancer = no )')
    print(jt.query('severe_headaches',[b_evidence, m_evidence]))









