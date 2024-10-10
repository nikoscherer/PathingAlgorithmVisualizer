import pygame
import sys

from Map import Map
from Node import Node

WINDOW_HEIGHT = 1280
WINDOW_WIDTH = 1280

BLACK = (30, 30, 30)

# _mapSize represented in (longitude,latitude), same for each node coordinate.
map = Map([5, 5], [WINDOW_WIDTH, WINDOW_HEIGHT], [Node([0, 0], 0), Node([1, 1], 1), Node([1, -1], 2)])

map.connect(0, 1)
map.connect(1, 2)

def main():
    map.init()

    while True:
        map.loop()


main()