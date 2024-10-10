import pygame
import sys

from Map import Map
from Node import Node

from BreadthFirstSearch import BreadthFirstSearch

WINDOW_HEIGHT = 1280
WINDOW_WIDTH = 1280

BLACK = (30, 30, 30)

# _mapSize represented in (longitude,latitude), same for each node coordinate.
map = Map([8, 8], [WINDOW_WIDTH, WINDOW_HEIGHT], 
        [
            Node([0, 0], 0), 
            Node([1, 1], 1), 
            Node([1, -1], 2), 
            Node([0, -1], 3), 
            Node([2, 2], 4),
            Node([3, 3], 5),
            Node([3, 2], 6)
        ])

bfs = BreadthFirstSearch(map)

map.setStartAndEnd(0, 3)
map.setAlgorithm(bfs)

map.connect(0, 1)
map.connect(1, 2)
map.connect(2, 0)
map.connect(2, 3)
map.connect(1, 4)
map.connect(4, 5)
map.connect(5, 6)

def main():
    map.init()

    while True:
        map.loop()


main()