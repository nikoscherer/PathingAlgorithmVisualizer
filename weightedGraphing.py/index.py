import pygame
import sys

from Map import Map
from Node import Node

from BreadthFirstSearch import BreadthFirstSearch

import osmnx as ox

from Utils import Places

# Variables
WINDOW_HEIGHT = 1280
WINDOW_WIDTH = 1280

bBox = [.3, .3]

path = True


place = Places.Italy.ROME

# Create nodes based off of osmnx
G = ox.graph_from_place(place, network_type='drive')
geocode = ox.geocode(place)
graphNodes = G.nodes(data=True)

nodes = []

for id, node in graphNodes:
    nodes.append(Node([node['x'], node['y']], id))

# _mapSize represented in (longitude,latitude), same for each node coordinate.
map = Map(bBox, [WINDOW_WIDTH, WINDOW_HEIGHT], nodes, [nodes[0].pos[0], nodes[0].pos[1]])

for id, node in graphNodes:
    neighbors = list(G.neighbors(id))
    for neighbor in neighbors:
        map.connect(id, neighbor)

bfs = BreadthFirstSearch(map)

map.setStartAndEnd(ox.nearest_nodes(G, geocode[1] + .01, geocode[0]), ox.nearest_nodes(G, geocode[1] + .03, geocode[0] + .03))
map.setAlgorithm(bfs)

def main():
    map.init()

    while True:
        map.loop(path)


main()