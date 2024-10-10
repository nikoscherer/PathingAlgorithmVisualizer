class BreadthFirstSearch:
    def __init__(self, _graph):
        self.graph = _graph
        self.curr = None
        self.visited = set()
        self.queue = []
        self.done = False
        self.parent = {}


    def search(self, searched, start, target):
        if self.curr is None:
            self.curr = start
            self.queue.append(start)
            
        if(len(self.queue) != 0):
            if self.curr not in self.visited:
                self.parent[self.queue[0]] = self.curr

            self.curr = self.queue[0]

            if(self.curr == target):
                print("FOUND")
                self.done = True
                return
            
            self.queue.pop(0)
            
            if self.curr not in self.visited:
                self.visited.add(self.curr)
                searched.append(self.curr)

            for adj in self.graph.vertMap[self.curr].adjacent:
                if adj not in self.queue and adj not in self.graph.obstacles and adj not in self.visited:
                    self.queue.append(adj)

        else:
            print("Done")