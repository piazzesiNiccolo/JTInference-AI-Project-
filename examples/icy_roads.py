from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

##ICY ROADS
def icy_roads_example():
    print('RUNNING ICY ROADS EXAMPLE \n\n')
    print('setting up network...')
    icy = TabularCPD('i',2,[[0.3],[0.7]])
    holmes = TabularCPD('h',2,[[0.9,0.2],[0.1,0.8]],['i'],[2])
    watson = TabularCPD('w',2,[[0.9,0.2],[0.1,0.8]],['i'],[2])
    print('setting up junction tree...')
    iw = Clique([icy,watson])
    ih = Clique([icy,holmes])

    jt2 = JunctionTree('t',[iw,ih])
    jt2.add_separator(iw,ih)

    print('\n\nICY\n')
    print('p(icy): ')
    print(jt2.query('i'))
    w_evidence = (watson,1)
    h_evidence = (holmes,0)
    print('p(icy|holmes = 0, watson = 1)')
    print(jt2.query('i',[h_evidence,w_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    jt2.init_tree()
    print('\n\nWATSON\n')
    print('p(watson): ')
    print(jt2.query('w'))
    h_evidence = (holmes,1)
    print('p(watson|holmes = YES)')
    print(jt2.query('w',[h_evidence]))


    input('\n PRESS ENTER TO RUN NEXT QUERY')
    jt2.init_tree()
    print('\n\nHOLMES\n')
    print('p(holmes): ')
    print(jt2.query('h'))
    i_evidence = (icy,0)
    print('p(holmes|icy = no)')
    print(jt2.query('h',[i_evidence]))
