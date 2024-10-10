import math

# Variables
class Color:
    BLACK = (30, 30, 30)
    WHITE = (225, 225, 225)


# Math Functions
def calculateWeight(n1, n2):
    return math.sqrt(pow(n1, 2) + pow(n2, 2))

def calculatePos(n1, n2, t):
    return [
        (1-t)*n1.x
    ]