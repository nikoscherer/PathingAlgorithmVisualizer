class BreadthFirstSearch:
    def __init__(self, _graph):
        self.graph = _graph


    def search(self, searched, start, target):
        if self.curr is None:
            self.curr = start
            self.visited = {}
            self.queue = {}

            self.queue.append(start)
            
        if(len(self.queue) != 0):
            curr = self.queue[0]

            if(curr == target):
                print("FOUND")

            for adj in curr.adjacent:
                if(not adj in searched):
                    self.queue.append(adj)

            searched.append(curr)
            self.queue.pop()

        else:
            print("NOT FOUND")
