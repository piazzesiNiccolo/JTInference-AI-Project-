from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

def flood_example():
    print('RUNNING FLOOD EXAMPLE\n\n')
    print('setting up network...')

    rain = TabularCPD('rain',2,[[0.99],[0.01]],state_names={'rain':['no', 'yes']})
    
    burglary = TabularCPD('burglary',2,[[0.5],[0.5]],state_names={'burglary':['no','yes']})
    
    earthquake = TabularCPD('earthquake',2,[[0.9],[0.1]],state_names={'burglary':['no','yes']})
    
    flood = TabularCPD('flood',2,[[1, 0.9],[0, 0.1]],['rain'],[2],
                            state_names={'flood':['no','yes'], 'rain':['no', 'yes']})
    
    alarm = TabularCPD('alarm',2,[[0.99, 0.01, 0.01, 0, 0.01, 0, 0, 0],[0.01, 0.99, 0.99, 1, 0.99, 1, 1, 1]],
                            ['earthquake','burglary','flood'],[2, 2, 2],
                            state_names={'alarm':['no','yes'],'earthquake':['no', 'yes'], 'burglary':['no', 'yes'], 'flood':['no', 'yes']})
    
    seismometer = TabularCPD('seismometer', 3,[[0.97, 0.01, 0.01, 0], [0.02, 0.97, 0.02, 0.03], [0.01, 0.02, 0.97, 0.97]],
                                 ['burglary', 'earthquake'],[2, 2],
                                 {'burglary':['no', 'yes'], 'earthquake':['no', 'yes']})

    print('setting up junction tree...')
    feba = Clique([flood,earthquake, burglary, alarm])
    ebs = Clique([earthquake, burglary, seismometer])
    fr = Clique([flood, rain])
    
    tree = JunctionTree('flood_tree', [feba,ebs,fr], fr)
    tree.add_separator(feba, ebs)
    tree.add_separator(feba, fr)

    print('\n\nRAIN\n')
    print('p(rain): ')
    print(tree.query('rain'))
    a_evidence = (alarm, 1)
    print('p(rain|alarm = yes)')
    print(tree.query('rain',[a_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nBURGLARY\n')
    print('p(burglary): ')
    print(tree.query('burglary'))
    s_evidence = (seismometer, 1)
    print('p(burglary|alarm = yes, seismometer = 1)')
    print(tree.query('burglary',[a_evidence, s_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nEARTHQUAKE\n')
    print('p(earthquake): ')
    print(tree.query('earthquake'))
    b_evidence = (burglary, 0)
    print('p(earthquake|seismometer = 1, burglary = no)')
    print(tree.query('earthquake',[s_evidence, b_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nFLOOD\n')
    print('p(flood): ')
    print(tree.query('flood'))
    r_evidence = (rain, 1)
    print('p(flood|alarm = yes, rain = yes)')
    print(tree.query('flood',[a_evidence, r_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nALARM\n')
    print('p(alarm): ')
    print(tree.query('alarm'))
    e_evidence = (earthquake, 1)
    print('p(alarm|earthquake = yes)')
    print(tree.query('alarm',[e_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nSEISMOMETER\n')
    print('p(seismometer): ')
    print(tree.query('seismometer'))
    e_evidence = (earthquake, 0)
    print('p(seismometer|burglary = no, earthquake = no)')
    print(tree.query('seismometer',[e_evidence, b_evidence]))
