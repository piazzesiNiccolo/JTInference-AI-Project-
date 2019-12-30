from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge,EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.potential import Potential,PotentialUtil
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController
from inference import JTNode

a = BbnNode(Variable(0,'A',['ON','OFF']),[0.5,0.5])
b = BbnNode(Variable(1,'B',['ON','OFF']),[0.5,0.5,0.4,0.6])
c = BbnNode(Variable(2,'C',['ON','OFF']),[0.7,0.3,0.2,0.8])
d = BbnNode(Variable(3,'D',['ON','OFF']),[0.9,0.1,0.5,0.5])
e = BbnNode(Variable(4,'E',['ON','OFF']),[0.3,0.7,0.6,0.4])
f = BbnNode(Variable(5,'F',['ON','OFF']),[0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.01])
g = BbnNode(Variable(6,'G',['ON','OFF']),[0.8,0.2,0.1,0.9])
h = BbnNode(Variable(7,'H',['ON','OFF']),[0.5,0.95,0.95,0.5,0.95,0.05,0.95,0.05])
bbn= Bbn()
bbn = bbn\
    .add_node(a)\
    .add_node(b)\
    .add_node(c)\
    .add_node(d)\
    .add_node(e)\
    .add_node(f)\
    .add_node(g)\
    .add_node(h)\
    .add_edge(Edge(a,b,EdgeType.DIRECTED))\
    .add_edge(Edge(a,c,EdgeType.DIRECTED))\
    .add_edge(Edge(b,d,EdgeType.DIRECTED))\
    .add_edge(Edge(c,e,EdgeType.DIRECTED))\
    .add_edge(Edge(d,f,EdgeType.DIRECTED))\
    .add_edge(Edge(e,f,EdgeType.DIRECTED))\
    .add_edge(Edge(c,g,EdgeType.DIRECTED))\
    .add_edge(Edge(e,h,EdgeType.DIRECTED))\
    .add_edge(Edge(g,h,EdgeType.DIRECTED))\

jt = JTNode("BC",[b,c])
p = Potential()
ff = b.id
b.potential = PotentialUtil.get_potential(b,Bbn.get_parents(ff))

jt.init_potential(b)
print(jt.potential)


join_tree = InferenceController.apply(bbn)

ev = EvidenceBuilder().with_node(join_tree.get_bbn_node_by_name('A')).with_evidence('ON',1.0).build()
join_tree.set_observation(ev)
for node in join_tree.get_bbn_nodes():
    potential = join_tree.get_bbn_potential(node)
    print(potential)
    print('\n')
    