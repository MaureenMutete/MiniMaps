import networkx as nx
import matplotlib.pyplot as plt
from classes.gbfs import GBFSTraverser

G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph1.A","Ph1.B","STC","Phase2","J1","Phase3","Mada","ParkingLot"]

G.add_nodes_from(nodes)
G.nodes()

G.add_edge("SportsComplex","Siwaka",weight="450")

G.add_edge("Siwaka","Ph1.A",weight="10")
G.add_edge("Siwaka","Ph1.B",weight="230")

G.add_edge("Ph1.A","Mada",weight="50")
G.add_edge("Ph1.A","Ph1.B",weight="100")

G.add_edge("Ph1.B","STC",weight="50")
G.add_edge("Ph1.B","Phase2",weight="50")

G.add_edge("Phase2","Phase3",weight="500")
G.add_edge("Phase2","J1",weight="600")
G.add_edge("Phase2","STC",weight="50")

G.add_edge("Phase3","ParkingLot",weight="500")

G.add_edge("J1","Mada",weight="200")

G.add_edge("STC","ParkingLot",weight="250")
G.add_edge("Mada","ParkingLot",weight="700")

G.nodes["SportsComplex"]['pos']=(0,0)
G.nodes["Siwaka"]['pos']=(3,0)
G.nodes["Ph1.A"]['pos']=(6,0)
G.nodes["Ph1.B"]['pos']=(4,-3)
G.nodes["Phase2"]['pos']=(8,-3)
G.nodes["J1"]['pos']=(12,-3)
G.nodes["Mada"]['pos']=(16,-3)
G.nodes["STC"]['pos']=(6,-6)
G.nodes["Phase3"]['pos']=(12,-6)
G.nodes["ParkingLot"]['pos']=(12,-9)



heuristic = {
    "SportsComplex": 730,
    "Siwaka": 405,
    "Ph1.A": 380,
    "Ph1.B": 280,
    "STC": 213,
    "Phase2": 210,
    "J1": 500,
    "Phase3": 160,
    "Mada": 630,
    "ParkingLot":0

}

node_pos = nx.get_node_attributes(G,'pos')
#call BFS to return set of all possible routes to the goal
#change this section to call whichever search algorithm that
#you have coded in classes (DFS,UCS,G-BFS,A*)
route_gbfs = GBFSTraverser(G, heuristic)
routes = route_gbfs.GBFS("SportsComplex","ParkingLot") #Define source and destination
print(route_gbfs.visited)
route_list = route_gbfs.visited
#color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()



