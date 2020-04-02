
from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

##setup tables
def mrs_gibbon_example():
    print('RUNNING MRS GIBBON EXAMPLE\n\n')
    print('setting up network...')
    rain = TabularCPD("r",2,[[0.9],[0.1]])
    sprinkler  = TabularCPD("s",2,[[0.9],[0.1]])
    watson = TabularCPD('w',2,[[0.9,0.01],[0.1,0.99]],['r'],[2])
    holmes = TabularCPD('h', 2,[[1,0.01, 0.1, 0],[0,0.99 ,0.9, 1]],['s', 'r'], [2, 2])
    gibbon = TabularCPD('g',2,[[0.9,0.01],[0.1,0.99]],['r'],[2])
    print('setting up junction tree...')
    #setup tree
    rg = Clique([rain,gibbon])
    rhs = Clique([rain,holmes,sprinkler])
    rw = Clique([rain,watson])
    jt = JunctionTree('tree',[rg,rhs,rw],rg)
    jt.add_separator(rg,rhs)
    jt.add_separator(rg,rw)

    #run queries
    print('\n\nHOLMES:\n')
    ##h query
    print('p(holmes)')
    print(jt.query('h'))
    print('\np(holmes|watson = yes, sprinkler = yes)')
    w_evidence = (watson,1)
    s_evidence = (sprinkler, 1)
    print(jt.query('h',[w_evidence,s_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    print('\n\nWATSON:\n')
    jt.init_tree()
    print('p(watson)')
    print(jt.query('w'))
    print('p(watson|ibbon = yes, holmes = no)')
    g_evidence = (gibbon, 1)
    h_evidence = (holmes,0)
    print(jt.query('w',[g_evidence,h_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    print('\n\nRAIN:\n')
    #r query
    jt.init_tree()
    print('p(rain)')
    print(jt.query('r'))
    print('p(rain|watson = yes, holmes = yes)')
    h_evidence = (holmes, 1)
    print(jt.query('r',[w_evidence,h_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    print('\n\n SPRNKLER:\n')
    #s query
    jt.init_tree()
    print('p(sprinkler)')
    print(jt.query('s'))
    print('p(sprinkler|holmes = yes)')
    print(jt.query('s',[h_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    print('\n\n GIBBON:\n')
    jt.init_tree()
    print('p(gibbon)')
    print(jt.query('g'))
    print('p(g|watson = yes)')
    w_evidence = (watson, 1)
    print(jt.query('g',[w_evidence]))

