class Node:
    def __init__(self, _id, _adjacent, _obstacle):
        self.id = _id
        self.adjacent = _adjacent
        self.obstacle = _obstacle

    def setObstacle(self, _obstacle):
        self.obstacle = _obstacle