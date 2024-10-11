import pygame
import sys

import Utils
from Utils import Color

from Node import Node

import osmnx as ox

class Map:
    def __init__(self, _mapSize, _screenSize, _nodes):
        self.MAP_WIDTH = _mapSize[0]
        self.MAP_HEIGHT = _mapSize[1]

        self.WINDOW_WIDTH = _screenSize[0]
        self.WINDOW_HEIGHT = _screenSize[1]

        self.vertices = _nodes
        self.vertMap = {}

        for node in self.vertices:
            self.vertMap[node.id] = node

    def __init__(self, _mapSize, _screenSize, _nodes, _normal):
        self.MAP_WIDTH = _mapSize[0]
        self.MAP_HEIGHT = _mapSize[1]

        self.WINDOW_WIDTH = _screenSize[0]
        self.WINDOW_HEIGHT = _screenSize[1]

        self.vertices = _nodes
        self.vertMap = {}
        self.normal = _normal

        for node in self.vertices:
            node.pos[0] = node.pos[0] - self.normal[0]
            node.pos[1] = node.pos[1] - self.normal[1]
            self.vertMap[node.id] = node

    def setAlgorithm(self, _algorithm):
        self.algorithm = _algorithm

    def connect(self, id1, id2):
        if not id2 in self.vertMap[id1].neighbors:
            self.vertMap[id1].neighbors.append(id2)
            self.vertMap[id2].neighbors.append(id1)

    def setStartAndEnd(self, _start, _end):
        self.start = self.vertMap[_start]
        self.end = self.vertMap[_end]

    def setStart(self, _start):
        self.start = self.vertMap[_start]

    def setEnd(self, _end):
        self.end = self.vertMap[_end]

    def nearest_node(self, x, y):
        normalX = -((self.MAP_WIDTH / 2) - (x / self.WINDOW_WIDTH) * self.MAP_WIDTH)
        normalY = (self.MAP_HEIGHT / 2) - (y / self.WINDOW_HEIGHT) * self.MAP_HEIGHT

        nearest = None
        minDist = float('inf')

        for node in self.vertices:
            dist = Utils.calculateDistance(normalX, normalY, node.pos[0], node.pos[1])

            if dist < minDist:
                nearest = node.id
                minDist = dist

        print(f'Nearest node: {nearest}, Distance: {minDist}')
        return nearest
        


    def init(self):
        global SCREEN, CLOCK

        SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        CLOCK = pygame.time.Clock()
        SCREEN.fill(Color.BLACK)

    def drawMap(self):
        SCREEN.fill(Color.BLACK)

        # Draw Edges
        for node in self.vertices:
            for id in node.neighbors:
                neighbor = self.vertMap[id]

                normalized1 = [
                    ((node.pos[0] + self.MAP_WIDTH / 2) / self.MAP_WIDTH) * self.WINDOW_WIDTH,
                    self.WINDOW_HEIGHT - ((node.pos[1] + self.MAP_HEIGHT / 2) / self.MAP_HEIGHT) * self.WINDOW_HEIGHT
                ]
                normalized2 = [
                    ((neighbor.pos[0] + self.MAP_WIDTH / 2) / self.MAP_WIDTH) * self.WINDOW_WIDTH,
                    self.WINDOW_HEIGHT - ((neighbor.pos[1] + self.MAP_HEIGHT / 2) / self.MAP_HEIGHT) * self.WINDOW_HEIGHT
                ]

                color = Color.WHITE

                if node.id in self.algorithm.visited and id in self.algorithm.visited:
                    color = Color.VISITED

                pygame.draw.line(SCREEN, color, normalized1, normalized2, 2)

        # Draw Nodes
        for node in self.vertices:
            color = Color.WHITE
            radius = 1

            # Normalize location
            normalized = [
                ((node.pos[0] + self.MAP_WIDTH / 2) / self.MAP_WIDTH) * self.WINDOW_WIDTH,
                self.WINDOW_HEIGHT - ((node.pos[1] + self.MAP_HEIGHT / 2) / self.MAP_HEIGHT) * self.WINDOW_HEIGHT
            ]

            # Check type to change color
            if node.id in self.algorithm.visited:
                color = Color.VISITED
                pygame.draw.circle(SCREEN, color, radius=1, center=normalized)
            if node == self.start:
                color = Color.START
                radius = 5
            if node == self.end:
                color = Color.TARGET
                radius = 5

            pygame.draw.circle(SCREEN, color, radius=radius, center=normalized)



    def loop(self, search):
        if search:
            self.algorithm.search(self.start.id, self.end.id)

        self.drawMap()

        pygame.display.update()