import pygame
import sys

from Types.Graph import Graph
from BreadthFirstSearch import BreadthFirstSearch

BLACK = (35, 35, 35)
WHITE = (180, 180, 180)

START = (255, 125, 29)
SEARCHED = (255, 215, 29)
TARGET = (255, 79, 29)

searched = {}

WINDOW_HEIGHT = 1200
WINDOW_WIDTH = 1200

# Variables
GRID_WIDTH = 20
GRID_HEIGHT = 20

startNode = [0, 0]
targetNode = [GRID_WIDTH - 10, GRID_HEIGHT - 5]

grid = []

for y in range(GRID_WIDTH):
    for x in range(GRID_HEIGHT):
        grid.append(x + (y * GRID_HEIGHT))

print(grid)

graph = Graph(grid)

for y in range(0, GRID_HEIGHT):
    for x in range(0, GRID_WIDTH):
        id = x + (y * GRID_HEIGHT)

        top = id - GRID_WIDTH
        right = id + 1
        bottom = id + GRID_HEIGHT
        left = id - 1

        if(top >= 0): # IF PAST FIRST NODE
            graph.connect(id, top)
        if((right != GRID_WIDTH * (y + 1))): # IF ON SAME HEIGHT
            graph.connect(id, right)
        if(bottom < GRID_WIDTH * GRID_HEIGHT): # IF PAST BOTTOM
            graph.connect(id, bottom)
        if((left != (GRID_WIDTH * y) - 1) and (left >= 0)): # IF ON SAME HEIGHT
            graph.connect(id, left)

bfs = BreadthFirstSearch(graph)



def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        bfs.search(searched, startNode[0] + (startNode[1] * GRID_WIDTH), targetNode[0] + (targetNode[1] * GRID_WIDTH))

        drawGrid(searched)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

        pygame.time.wait(500)


def drawGrid(searched):
    for x in range(0, WINDOW_WIDTH, int(WINDOW_WIDTH / GRID_WIDTH)):
        for y in range(0, WINDOW_HEIGHT, int(WINDOW_HEIGHT / GRID_HEIGHT)):
            rect = pygame.Rect(x, y, WINDOW_WIDTH / GRID_WIDTH, WINDOW_HEIGHT / GRID_HEIGHT)

            color = BLACK
            if(x == startNode[0] * (WINDOW_WIDTH / GRID_WIDTH) and y == startNode[1] * (WINDOW_HEIGHT / GRID_HEIGHT)):
                color = START
            elif(x == targetNode[0] * (WINDOW_WIDTH / GRID_WIDTH) and y == targetNode[1] * (WINDOW_HEIGHT / GRID_HEIGHT)):
                color = TARGET
            else:
                if (x + (y * GRID_HEIGHT) * (WINDOW_WIDTH / GRID_WIDTH)) in searched:
                    color = SEARCHED

            pygame.draw.rect(SCREEN, color, rect)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)





main()