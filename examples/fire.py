from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

#setup nodes
def fire_example():
    print('RUNNING FIRE EXAMPLE\n\n')
    
    print('setting up network...')
    fire = TabularCPD('f',2,[[0.99],[0.01]],state_names={'f':['no','yes']})
    
    tampering = TabularCPD('t',2,[[0.98], [0.02]], state_names={'t':['no','yes']})
    
    smoke = TabularCPD('s',2 ,[[0.99, 0.1], [0.01,0.9]],['f'],[2], 
                            state_names={'s':['no','yes'], 'f':['no', 'yes']})
    
    alarm = TabularCPD('a',2 ,[[0.9999, 0.15, 0.01, 0.5], [0.0001,0.85,0.99, 0.5]],['f','t'],[2,2],
                            state_names={'a':['no','yes'], 'f':['no', 'yes'], 't':['no','yes']})
    
    leaving = TabularCPD('l',2 ,[[0.999, 0.12], [0.001,0.88]],['a'],[2],
                            state_names={'l':['no','yes'], 'a':['no', 'yes']})
    
    report = TabularCPD('r', 2 ,[[0.99, 0.25], [0.01,0.75]],['l'],[2],
                            state_names={'r':['no','yes'], 'l':['no', 'yes']})
    print('setting up tree...')
    #setup tree
    la = Clique([leaving,alarm])
    aft = Clique([alarm,fire,tampering])
    lr = Clique([leaving,report])
    fs = Clique([fire,smoke])
    tree = JunctionTree('fire_tree',[la,aft,lr,fs])
    tree.add_separator(la,aft)
    tree.add_separator(la,lr)
    tree.add_separator(aft,fs)
    print('running queries...')


    print('\n\nFIRE\n')
    print('p(fire)')
    print(tree.query('f'))
    l_evidence = (leaving, 1)
    a_evidence = (alarm, 1)
    print('p(fire|leaving = 1, alarm = 1)')
    print(tree.query('f',[l_evidence,a_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\n TAMPERING\n')
    print('p(tampering)')
    print(tree.query('t'))
    r_evidence = (report, 1)
    s_evidence = (smoke, 0)
    print('p(tampering|report = 1, smoke = 0)')
    print(tree.query('t',[r_evidence,s_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nSMOKE\n')
    print('p(smoke)')
    print(tree.query('s'))
    f_evidence = (fire, 1)
    l_evidence = (leaving, 0)
    print('p(smoke|fire = 1, leaving = 0)')
    print(tree.query('s',[f_evidence,l_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nALARM\n')
    print('p(alarm)')
    print(tree.query('a'))
    r_evidence = (report, 1)
    s_evidence = (smoke, 0)
    print('p(alarm|report = 1, smoke = 0)')
    print(tree.query('a',[r_evidence,s_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nLEAVING\n')
    print('p(leaving)')
    print(tree.query('l'))
    f_evidence = (fire, 1)
    t_evidence = (tampering, 1)
    print('p(tampering|report = 1, fire = 1, tampering = 1)')
    print(tree.query('l',[r_evidence,f_evidence, t_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nREPORT\n')
    print('p(report)')
    print(tree.query('r'))
    t_evidence = (tampering, 0)
    s_evidence = (smoke, 1)
    print('p(report|tampering = 0, smoke = 1)')
    print(tree.query('r',[t_evidence,s_evidence]))