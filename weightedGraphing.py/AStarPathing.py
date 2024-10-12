import Utils

class AStarPathing:
    def __init__(self, _map):
        self.map = _map
        self.curr = None
        self.visited = set()
        self.visit = []
        self.done = False
        self.parent = {}


    def search(self, start, target):
        if self.curr is None:
            self.start = start
            self.end = target
            self.curr = start
            self.visit.append(start)
            self.visited.add(start)

            for n in self.map.vertMap[start].neighbors:
                self.visit.append(n)

        if self.curr == target:
            print("DONE")
            self.done = True
            return

        startNode = self.map.vertMap[start]
        targetNode = self.map.vertMap[target]

        self.visit.remove(self.curr)
        self.visited.add(self.curr)

        closestID = None
        minCost = float('inf')
            
        for id in self.visit:
            node = self.map.vertMap[id]

            if id not in self.visited:
                gCost = Utils.calculateDistance(node.pos[0], node.pos[1], startNode.pos[0], startNode.pos[1])
                hCost = Utils.calculateDistance(node.pos[0], node.pos[1], targetNode.pos[0], targetNode.pos[1])
                fCost = hCost + gCost

                if fCost < minCost:
                    closestID = id
                    minCost = fCost

        for n in self.map.vertMap[self.curr].neighbors:
            if n not in self.visited:
                self.visit.append(n)

        self.parent[closestID] = self.curr
        self.curr = closestID

    def reconstructPath(self):
        path = [] 
        next = self.end

        while next in self.parent.keys():
            path.append(next) 
            next = self.parent[next]

        if next == self.start:
            path.append(self.start)

        return path