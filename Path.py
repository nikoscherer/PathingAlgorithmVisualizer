import pygame
import sys

from Types.UnweightedGraph import Graph
from BreadthFirstSearchOLD import BreadthFirstSearch
from DepthFirstSearch import DepthFirstSearch

WINDOW_HEIGHT = 1280
WINDOW_WIDTH = 1280

# Variables
GRID_WIDTH = 20
GRID_HEIGHT = 20

BLACK = (35, 35, 35)
WHITE = (180, 180, 180)
FULL_WHITE = (255, 255, 255)
TEXT = (100, 100, 100)

START = (255, 125, 29)
SEARCHED = (255, 215, 29)
TARGET = (255, 79, 29)

def createObstacleH(arr, firstID, secondID):
    for i in range (firstID, secondID + 1):
        arr.append(i)

def createObstacleV(arr, firstID, secondID):
    for i in range(firstID, secondID + GRID_HEIGHT, GRID_HEIGHT):
        arr.append(i)

obstacles = []

createObstacleH(obstacles, 21, 38)
createObstacleH(obstacles, 361, 361)
createObstacleH(obstacles, 363, 378)
createObstacleV(obstacles, 21, 361)
createObstacleV(obstacles, 38, 58)
createObstacleV(obstacles, 98, 378)

createObstacleH(obstacles, 276, 278)
createObstacleV(obstacles, 76, 336)
createObstacleH(obstacles, 62, 67)
createObstacleH(obstacles, 69, 76)
createObstacleV(obstacles, 67, 107)
createObstacleH(obstacles, 103, 107)
createObstacleH(obstacles, 141, 149)
createObstacleV(obstacles, 129, 149)
createObstacleV(obstacles, 69, 89)
createObstacleH(obstacles, 149, 154)
createObstacleH(obstacles, 111, 114)
createObstacleV(obstacles, 114, 154)

createObstacleV(obstacles, 183, 363)

createObstacleV(obstacles, 289, 329)
createObstacleV(obstacles, 287, 327)
createObstacleH(obstacles, 283, 285)
createObstacleV(obstacles, 285, 325)
createObstacleH(obstacles, 287, 289)
createObstacleH(obstacles, 329, 336)

searched = []

startNode = [0, 0]
targetNode = [GRID_WIDTH - 10, GRID_HEIGHT - 5]

grid = []

for y in range(GRID_WIDTH):
    for x in range(GRID_HEIGHT):
        grid.append(x + (y * GRID_HEIGHT))

print(grid)

graph = Graph(grid, obstacles)

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
dfs = DepthFirstSearch(graph)

pygame.init()
font = pygame.font.Font(None, 20)


def main():
    global SCREEN, CLOCK

    loop = 0

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        if loop >= 5 and not bfs.done:
            #dfs.search(searched, startNode[0] + (startNode[1] * GRID_WIDTH), targetNode[0] + (targetNode[1] * GRID_WIDTH))
            bfs.search(searched, startNode[0] + (startNode[1] * GRID_WIDTH), targetNode[0] + (targetNode[1] * GRID_WIDTH))
            loop = 0

        drawGrid(searched)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

        if not bfs.done:
            loop = loop + 1



def drawGrid(searched):
    for x in range(0, WINDOW_WIDTH, int(WINDOW_WIDTH / GRID_WIDTH)):
        for y in range(0, WINDOW_HEIGHT, int(WINDOW_HEIGHT / GRID_HEIGHT)):
            rect = pygame.Rect(x, y, WINDOW_WIDTH / GRID_WIDTH, WINDOW_HEIGHT / GRID_HEIGHT)

            id = (x // (WINDOW_WIDTH // GRID_WIDTH)) + \
                (y // (WINDOW_HEIGHT // GRID_HEIGHT)) * GRID_WIDTH

            color = BLACK
            if(x == startNode[0] * (WINDOW_WIDTH / GRID_WIDTH) and y == startNode[1] * (WINDOW_HEIGHT / GRID_HEIGHT)):
                color = START
            elif(x == targetNode[0] * (WINDOW_WIDTH / GRID_WIDTH) and y == targetNode[1] * (WINDOW_HEIGHT / GRID_HEIGHT)):
                color = TARGET
            else:
                
                if id in obstacles:
                    color = FULL_WHITE
                if id in searched:
                    color = SEARCHED

            pygame.draw.rect(SCREEN, color, rect)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

            id_text = font.render(str(id), True, TEXT)
            corner = rect.bottomleft
            calc = [
                corner[0] + (rect.centerx - corner[0]) / 3,
                corner[1] + (rect.centery - corner[1]) / 3,
            ]
            text_rect = id_text.get_rect(center=calc)
            SCREEN.blit(id_text, text_rect)
            
main()