import networkx as nx
vert = 'abcdefg'
graph = {'a': ('b', 'f'),
         'b': ('a', 'c', 'g'),
         'c': ('b', 'd', 'e', 'g'),
         'd': ('c', 'e'),
         'e': ('c', 'd', 'f', 'g'),
         'f': ('a', 'e', 'g'),
         'g': ('b', 'c', 'e', 'f')
         }
GRAPH = nx.Graph()
for i in vert:
    GRAPH.add_node(i)
    GRAPH.add_edge(i, graph[i])
print("Nodes: " + str(GRAPH.nodes()))
print("Edges: " + str(GRAPH.edges()))
