class DepthFirstSearch:
    def __init__(self, _graph):
        self.graph = _graph
        self.curr = None
        self.visited = set()
        self.queue = []


    def search(self, searched, start, target):
        if self.curr is None:
            self.curr = start
            self.queue.append(start)
            
        if(len(self.queue) != 0):
            curr = self.queue[len(self.queue) - 1]

            if(curr == target):
                print("FOUND")
                return
            
            self.queue.pop(len(self.queue) - 1)
            
            if curr not in self.visited:
                self.visited.add(curr)
                searched.append(curr)

            for adj in self.graph.vertMap[curr].adjacent:
                if adj not in self.queue and adj not in self.graph.obstacles and adj not in self.visited:
                    self.queue.append(adj)

        else:
            print("Done")