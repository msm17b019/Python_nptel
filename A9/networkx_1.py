import networkx as nx 
import matplotlib.pyplot as plt  


G=nx.Graph()

G=nx.complete_graph(10)

# G.add_node(1)
# G.add_node(2)
# G.add_node(3)

# G.add_edge(1,2)
# G.add_edge(2,3)
# G.add_edge(3,1)

nx.draw(G)
plt.show()

