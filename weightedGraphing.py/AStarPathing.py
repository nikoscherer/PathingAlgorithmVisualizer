import Utils

import heapq

class AStarPathing:
    def __init__(self, _map):
        self.map = _map
        self.curr = None
        self.visited = set()
        self.visit = []
        self.inVisit = set()
        self.done = False
        self.parent = {}

    def calculateCost(self, startNode, node, targetNode):
        gCost = Utils.calculateDistance(node.pos[0], node.pos[1], startNode.pos[0], startNode.pos[1])
        hCost = Utils.calculateDistance(node.pos[0], node.pos[1], targetNode.pos[0], targetNode.pos[1])

        return hCost + gCost

    def search(self, start, target):
        if self.curr is None:
            self.start = start
            self.end = target
            self.curr = None
            heapq.heappush(self.visit, (0, start))
            self.inVisit.add(start)
        
        self.curr = heapq.heappop(self.visit)[1]
        self.inVisit.remove(self.curr)
        self.visited.add(self.curr)

        if self.curr == target:
            print("DONE")
            self.done = True
            return

        startNode = self.map.vertMap[start]
        targetNode = self.map.vertMap[target]

        for neighbor in self.map.vertMap[self.curr].neighbors:
            if neighbor not in self.visited and neighbor not in self.inVisit:
                node = self.map.vertMap[neighbor]

                fCost = self.calculateCost(startNode, node, targetNode)

                heapq.heappush(self.visit, (fCost, neighbor))
                self.inVisit.add(neighbor)

                self.parent[neighbor] = self.curr
    def reconstructPath(self):
        path = [] 
        next = self.end

        while next in self.parent.keys():
            path.append(next) 
            next = self.parent[next]

        if next == self.start:
            path.append(self.start)

        return path