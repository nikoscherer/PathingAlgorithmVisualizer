import pygame
import sys

from Map import Map
from Node import Node

from BreadthFirstSearch import BreadthFirstSearch
from AStarPathing import AStarPathing

import osmnx as ox

from Utils import Places

# Variables
WINDOW_HEIGHT = 1280
WINDOW_WIDTH = 1280

bBox = [0.15, 0.15]

path = False


place = Places.Italy.ROME

# Change to graph_from_bbox
G = ox.graph_from_place(place, network_type='drive', retain_all=True)
geocode = ox.geocode(place)
graphNodes = G.nodes(data=True)

print(geocode)

nodes = []

for id, node in graphNodes:
    nodes.append(Node([node['x'], node['y']], id))

map = Map(bBox, [WINDOW_WIDTH, WINDOW_HEIGHT], nodes, [nodes[0].pos[0], nodes[0].pos[1] + .06])

for id, node in graphNodes:
    neighbors = list(G.neighbors(id))
    for neighbor in neighbors:
        map.connect(id, neighbor)

#bfs = BreadthFirstSearch(map)
aStar = AStarPathing(map)

map.setAlgorithm(aStar)
map.setStartAndEnd(ox.nearest_nodes(G, geocode[1], geocode[0]), ox.nearest_nodes(G, geocode[1] + .03, geocode[0] + .03))

def main():
    global path

    map.init()

    while True:
        map.loop(path)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]

                if event.button == 1: # LEFT CLICK
                    nearest = map.nearest_node(pos[0], pos[1])
                    map.setStart(nearest)
                elif event.button == 3: # RIGHT CLICK
                    nearest = map.nearest_node(pos[0], pos[1])
                    map.setEnd(nearest)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                path = True

main()