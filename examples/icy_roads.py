from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

##ICY ROADS
def icy_roads_example():
    print('RUNNING ICY ROADS EXAMPLE \n\n')
    print('setting up network...')
    
    icy = TabularCPD('icy',2,[[0.3],[0.7]],state_names={'icy':['no','yes']})
    
    holmes = TabularCPD('holmes',2,[[0.9,0.2],[0.1,0.8]],['icy'],[2],{'holmes':['no','yes'],'icy':['no','yes']})
    
    watson = TabularCPD('watson',2,[[0.9,0.2],[0.1,0.8]],['icy'],[2],{'watson':['no','yes'],'icy':['no', 'yes']})
    
    print('setting up junction tree...')
    iw = Clique([icy,watson])
    ih = Clique([icy,holmes])
    jt2 = JunctionTree('t',[iw,ih])
    jt2.add_separator(iw,ih)

    print('\n\nICY\n')
    print('p(icy): ')
    print(jt2.query('icy'))
    w_evidence = (watson,1)
    h_evidence = (holmes,0)
    print('p(icy|holmes = no, watson = yes)')
    print(jt2.query('icy',[h_evidence,w_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    jt2.init_tree()
    print('\n\nWATSON\n')
    print('p(watson): ')
    print(jt2.query('watson'))
    h_evidence = (holmes,1)
    print('p(watson|holmes = yes)')
    print(jt2.query('watson',[h_evidence]))


    input('\n PRESS ENTER TO RUN NEXT QUERY')
    jt2.init_tree()
    print('\n\nHOLMES\n')
    print('p(holmes): ')
    print(jt2.query('holmes'))
    i_evidence = (icy,0)
    print('p(holmes|icy = no)')
    print(jt2.query('holmes',[i_evidence]))
