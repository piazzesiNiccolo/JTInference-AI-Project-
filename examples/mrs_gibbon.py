
from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

##setup tables
def mrs_gibbon_example():
    print('RUNNING MRS GIBBON EXAMPLE\n\n')
    print('setting up network...')
    
    rain = TabularCPD('rain',2,[[0.9],[0.1]],state_names={'rain':['no', 'yes']})
    
    sprinkler  = TabularCPD('sprinkler',2,[[0.9],[0.1]],state_names={'sprinkler':['no', 'yes']})
    
    watson = TabularCPD('watson',2,[[0.9,0.01],[0.1,0.99]],['rain'],[2],
                            state_names={'watson':['no','yes'], 'rain':['no', 'yes']})
    
    holmes = TabularCPD('holmes', 2,[[1,0.01, 0.1, 0],[0,0.99 ,0.9, 1]],['sprinkler', 'rain'], [2, 2],
                            state_names={'holmes':['no', 'yes'],'sprinkler':['no','yes'],'rain':['no', 'yes']})
    
    gibbon = TabularCPD('gibbon',2,[[0.9,0.01],[0.1,0.99]],['rain'],[2],
                            state_names={'gibbon':['no','yes'], 'rain':['no', 'yes']})
    
    print('setting up junction tree...')
    rg = Clique([rain,gibbon])
    rhs = Clique([rain,holmes,sprinkler])
    rw = Clique([rain,watson])
    
    jt = JunctionTree('gibbon_tree',[rg,rhs,rw],rg)
    jt.add_separator(rg,rhs)
    jt.add_separator(rg,rw)

    #run queries
    print('\n\nHOLMES:\n')
    ##h query
    print('p(holmes)')
    print(jt.query('holmes'))
    print('\np(holmes|watson = yes, sprinkler = yes)')
    w_evidence = (watson,1)
    s_evidence = (sprinkler, 1)
    print(jt.query('holmes',[w_evidence,s_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    print('\n\nWATSON:\n')
    jt.init_tree()
    print('p(watson)')
    print(jt.query('watson'))
    print('p(watson|gibbon = yes, holmes = no)')
    g_evidence = (gibbon, 1)
    h_evidence = (holmes,0)
    print(jt.query('watson',[g_evidence,h_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    print('\n\nRAIN:\n')
    #r query
    jt.init_tree()
    print('p(rain)')
    print(jt.query('rain'))
    print('p(rain|watson = yes, holmes = yes)')
    h_evidence = (holmes, 1)
    print(jt.query('rain',[w_evidence,h_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    print('\n\n SPRNKLER:\n')
    #s query
    jt.init_tree()
    print('p(sprinkler)')
    print(jt.query('sprinkler'))
    print('p(sprinkler|holmes = yes)')
    print(jt.query('sprinkler',[h_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    print('\n\n GIBBON:\n')
    jt.init_tree()
    print('p(gibbon)')
    print(jt.query('gibbon'))
    print('p(gibbon|watson = yes)')
    w_evidence = (watson, 1)
    print(jt.query('gibbon',[w_evidence]))

