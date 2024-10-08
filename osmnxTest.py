from matplotlib.animation import FuncAnimation
import osmnx as ox
import networkx as nx
from osmnx import distance
import matplotlib.pyplot as plt

places = [
    'Manhattan, New York, USA',
    'Modena, Italy',
    'Alberobello, Italy',
    'Rome, Italy'
]

place_name = places[2]
#G = ox.graph_from_bbox(north=38.11, west=13.31, south=38.08, east=13.36, simplify=True, retain_all=False, network_type="drive")
G = ox.graph_from_place(place_name, network_type="drive")


start = (38.106, 13.361)
end = (38.10389, 13.32)

node_id = ox.nearest_nodes(G, X=start[1], Y=start[0])

print(node_id)

neighbors = list(nx.neighbors(G, node_id))

routes = [[node_id]]
visited = set()
queue = [node_id]

fig, ax = ox.plot_graph(G, figsize=(16, 16), show=False, close=False)

def update(frame):
    global queue
    if not queue:
        return
    
    currentNode = queue.pop(len(queue) - 1)
    visited.add(currentNode)

    neighbors = list(nx.neighbors(G, currentNode))

    for neighbor in neighbors:
        if neighbor not in visited and neighbor not in queue:
            if G.has_edge(currentNode, neighbor) or G.has_edge(neighbor, currentNode):
                queue.append(neighbor)
 
    routes[0].append(currentNode)

    ax.clear()
    ox.plot_graph(G, ax=ax, show=False, close=False)
    if len(routes[0]) > 1:
        ox.plot_graph_route(G, route=routes[0], ax=ax, route_color='orange', show=False, close=False)


#fig, ax = ox.plot_graph(G, figsize=(12, 12))
#fig, ax = ox.plot_graph_route(G, route=routes[0], figsize=(16, 16), route_color='orange')

animation = FuncAnimation(fig, update, frames=100, repeat=False)

plt.show()