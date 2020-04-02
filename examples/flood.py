from tree.node import Clique,Separator
from tree.junction_tree import JunctionTree
from pgmpy.factors.discrete.CPD import TabularCPD

def flood_example():
    print('RUNNING FLOOD EXAMPLE\n\n')
    print('setting up network...')

    rain = TabularCPD('r',2,[[0.99],[0.01]])
    burglary = TabularCPD('b',2,[[0.5],[0.5]])
    earthquake = TabularCPD('e',2,[[0.9],[0.1]])
    flood = TabularCPD('f',2,[[1, 0.9],[0, 0.1]],['r'],[2])
    alarm = TabularCPD('a',2,[[0.99, 0.01, 0.01, 0, 0.01, 0, 0, 0],[0.01, 0.99, 0.99, 1, 0.99, 1, 1, 1]],['e','b','f'],[2, 2, 2])
    seismometer = TabularCPD('s', 3,[[0.97, 0.01, 0.01, 0], [0.02, 0.97, 0.02, 0.03], [0.01, 0.02, 0.97, 0.97]], ['b', 'e'],[2, 2])

    print('setting up junction tree...')
    feba = Clique([flood,earthquake, burglary, alarm])
    ebs = Clique([earthquake, burglary, seismometer])
    fr = Clique([flood, rain])
    tree = JunctionTree('tree', [feba,ebs,fr], feba)
    tree.add_separator(feba, ebs)
    tree.add_separator(feba, fr)

    print('\n\nRAIN\n')
    print('p(rain): ')
    print(tree.query('r'))
    a_evidence = (alarm, 1)
    print('p(rain|alarm = 1)')
    print(tree.query('r',[a_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nBURGLARY\n')
    print('p(burglary): ')
    print(tree.query('b'))
    s_evidence = (seismometer, 1)
    print('p(burglary|alarm = yes, seismometer = 1)')
    print(tree.query('b',[a_evidence, s_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nEARTHQUAKE\n')
    print('p(earthquake): ')
    print(tree.query('e'))
    b_evidence = (burglary, 0)
    print('p(earthquake|seismometer = 1, burglary = no)')
    print(tree.query('e',[s_evidence, b_evidence]))

    tree.init_tree()
    print('\n\nFLOOD\n')
    print('p(flood): ')
    print(tree.query('f'))
    r_evidence = (rain, 1)
    print('p(flood|alarm = yes, rain = yes)')
    print(tree.query('f',[a_evidence, r_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nALARM\n')
    print('p(alarm): ')
    print(tree.query('a'))
    e_evidence = (earthquake, 1)
    print('p(alarm|earthquake = yes)')
    print(tree.query('a',[e_evidence]))

    input('\n PRESS ENTER TO RUN NEXT QUERY')
    tree.init_tree()
    print('\n\nSEISMOMETER\n')
    print('p(seismometer): ')
    print(tree.query('s'))
    e_evidence = (earthquake, 0)
    print('p(seismometer|burglary = no, earthquake = no)')
    print(tree.query('s',[e_evidence, e_evidence]))
