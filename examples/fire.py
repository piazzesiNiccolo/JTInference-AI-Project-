from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD


def fire_example():
    print('RUNNING FIRE EXAMPLE\n\n')
    
    print('setting up network...')
    fire = TabularCPD('fire',2,[[0.99],[0.01]],state_names={'fire':['false','true']})
    
    tampering = TabularCPD('tampering',2,[[0.98], [0.02]], state_names={'tampering':['false','true']})
    
    smoke = TabularCPD('smoke',2 ,[[0.99, 0.1], [0.01,0.9]],['fire'],[2], 
                            state_names={'smoke':['false','true'], 'fire':['false', 'true']})
    
    alarm = TabularCPD('alarm',2 ,[[0.9999, 0.15, 0.01, 0.5], [0.0001,0.85,0.99, 0.5]],['fire','tampering'],[2,2],
                            state_names={'alarm':['false','true'], 'fire':['false', 'true'], 'tampering':['false','true']})
    
    leaving = TabularCPD('leaving',2 ,[[0.999, 0.12], [0.001,0.88]],['alarm'],[2],
                            state_names={'leaving':['false','true'], 'alarm':['false', 'true']})
    
    report = TabularCPD('report', 2 ,[[0.99, 0.25], [0.01,0.75]],['leaving'],[2],
                            state_names={'report':['false','true'], 'leaving':['false', 'true']})
    print('setting up junction tree...')
    #setup tree
    la = Clique([leaving,alarm])
    aft = Clique([alarm,fire,tampering])
    lr = Clique([leaving,report])
    fs = Clique([fire,smoke])
    
    tree = JunctionTree('fire_tree',[la,aft,lr,fs],root=fs)
    tree.add_separator(la,aft)
    tree.add_separator(la,lr)
    tree.add_separator(aft,fs)


    print('\n\nFIRE\n')
    print('p(fire)')
    print(tree.query('fire'))
    l_evidence = (leaving, 1)
    a_evidence = (alarm, 1)
    print('p(fire|leaving = true, alarm = true)')
    print(tree.query('fire',[l_evidence,a_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\n TAMPERING\n')
    print('p(tampering)')
    print(tree.query('tampering'))
    r_evidence = (report, 1)
    s_evidence = (smoke, 0)
    print('p(tampering|report = true, smoke = false)')
    print(tree.query('tampering',[r_evidence,s_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nSMOKE\n')
    print('p(smoke)')
    print(tree.query('smoke'))
    f_evidence = (fire, 1)
    l_evidence = (leaving, 0)
    print('p(smoke|fire = true, leaving = false)')
    print(tree.query('smoke',[f_evidence,l_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nALARM\n')
    print('p(alarm)')
    print(tree.query('alarm'))
    r_evidence = (report, 1)
    s_evidence = (smoke, 0)
    print('p(alarm|report = true, smoke = false)')
    print(tree.query('alarm',[r_evidence,s_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nLEAVING\n')
    print('p(leaving)')
    print(tree.query('leaving'))
    r_evidence = (report, 0)
    f_evidence = (fire, 1)
    t_evidence = (tampering, 1)
    print('p(leaving|report = false, fire = true, tampering = true)')
    print(tree.query('leaving',[r_evidence,f_evidence, t_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nREPORT\n')
    print('p(report)')
    print(tree.query('report'))
    t_evidence = (tampering, 0)
    s_evidence = (smoke, 1)
    print('p(report|tampering = false, smoke = true)')
    print(tree.query('report',[t_evidence,s_evidence]))