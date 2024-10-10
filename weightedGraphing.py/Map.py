import pygame
import sys

import Utils
from Utils import Color

from Node import Node

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

    def setAlgorithm(self, _algorithm):
        self.algorithm = _algorithm

    def connect(self, id1, id2):
        if not id2 in self.vertMap[id1].neighbors:
            self.vertMap[id1].neighbors.append(id2)
            self.vertMap[id2].neighbors.append(id1)

    def setStartAndEnd(self, _start, _end):
        self.start = self.vertMap[_start]
        self.end = self.vertMap[_end]

    def init(self):
        global SCREEN, CLOCK

        SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        CLOCK = pygame.time.Clock()
        SCREEN.fill(Color.BLACK)

    def drawMap(self):
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

                pygame.draw.line(SCREEN, Color.WHITE, normalized1, normalized2, 2)

        # Draw Nodes
        for node in self.vertices:
            color = Color.WHITE

            # Normalize location
            normalized = [
                ((node.pos[0] + self.MAP_WIDTH / 2) / self.MAP_WIDTH) * self.WINDOW_WIDTH,
                self.WINDOW_HEIGHT - ((node.pos[1] + self.MAP_HEIGHT / 2) / self.MAP_HEIGHT) * self.WINDOW_HEIGHT
            ]

            # Check type to change color
            if node.id in self.algorithm.visited:
                color = Color.VISITED
            if node == self.start:
                color = Color.START
            if node == self.end:
                color = Color.TARGET

            pygame.draw.circle(SCREEN, color, radius=(7.5 * ((self.WINDOW_WIDTH + self.WINDOW_HEIGHT) / 2 / (1280))), center=normalized)
            ...
        ...


    def loop(self):
        searched = self.algorithm.search(self.start.id, self.end.id)
        self.drawMap()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

