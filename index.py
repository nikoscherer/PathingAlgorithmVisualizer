import pygame
import sys

from Types.UnweightedGraph import Graph
from BreadthFirstSearchOLD import BreadthFirstSearch
from DepthFirstSearch import DepthFirstSearch

WINDOW_HEIGHT = 1280
WINDOW_WIDTH = 1280

BLACK = (30, 30, 30)

pygame.init()

def main():
    global SCREEN, CLOCK

    loop = 0

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


main()