import math

# Variables
class Color:
    BLACK = (30, 30, 30)
    WHITE = (225, 225, 225)

    START = (255, 125, 29)
    VISITED = (255, 215, 29)
    TARGET = (255, 79, 29)

    DONE = (255, 79, 29)
    GRAY = (150, 150, 150)

class Places:
    class USA:
        MANHATTAN = 'Manhattan, New York, USA'
    class Italy:
        ROME = 'Rome, Italy'

# Math Functions
def calculateHypo(x, y):
    return math.sqrt(pow(x, 2) + pow(y, 2))

def calculateDistance(x1, y1, x2, y2):
    diff = [
        x2 - x1,
        y2 - y1
    ]
    return calculateHypo(diff[0], diff[1])

def calculatePos(n1, n2, t):
    return [
        (1-t)*n1.x
    ]