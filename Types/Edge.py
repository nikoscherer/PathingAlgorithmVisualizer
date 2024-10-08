class Edge:
    def __init__(self, _neighbors, _distance):
        self.neighbors = _neighbors
        self.distance = _distance

    def getOtherNeighbor(self, id):
        index = self.neighbors.index(id)

        if(index == 0):
            return 1
        
        return 0