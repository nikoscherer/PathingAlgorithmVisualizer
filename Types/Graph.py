from Types.Node import Node

class Graph:
    def __init__(self, _verticesID):
        self.vertices = []
        self.vertMap = {}

        for vert in _verticesID:    
            node = Node(vert, [])
            self.vertices.append(node)
            self.vertMap[vert] = self.vertices[len(self.vertices) - 1]

    def connect(self, id1, id2):
        if not id2 in self.vertMap[id1].adjacent:
            self.vertMap[id1].adjacent.append(id2)
            self.vertMap[id2].adjacent.append(id1)


    def simpleDisplay(self):
        for vert in self.vertices:
            print(f'{vert.id} : ', end='')

            for adj in vert.adjacent:
                print(adj, end=' ')

            print('')