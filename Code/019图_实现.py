# rt

# 定义vertex类
class Vertex():
    def __init__(self, value):
        self.value = value
        self.nexts = {}
    
    def addNext(self, to, weight = None):
        self.nexts[to] = weight
    
    def getNext(self):
        # return self.nexts.keys()
        return self.nexts.items()

class Graph():
    def __init__(self):
        self.vertexs = []

    def addVertex(self, value):
        tempVertex = Vertex(value)
        self.vertexs.append(tempVertex)

    def addEdge(self, From, to, weight = None):
        for i in self.vertexs:
            if i.value == From:
                i.addNext(to, weight)
            if i.value == to:
                i.addNext(From, weight)
    def getNexts(self, value):
        for i in self.vertexs:
            if i.value == value:
                return i.getNext()


if __name__ == '__main__':
    myGraph = Graph()
    myGraph.addVertex('A')
    myGraph.addVertex('B')
    myGraph.addVertex('C')
    myGraph.addVertex('D')
    myGraph.addVertex('E')
    myGraph.addVertex('F')
    myGraph.addEdge('A', 'B', 3)
    myGraph.addEdge('A', 'C', 15)
    myGraph.addEdge('A', 'D', 9)
    myGraph.addEdge('C', 'D', 2)
    myGraph.addEdge('C', 'B', 12)
    myGraph.addEdge('C', 'E', 14)
    myGraph.addEdge('E', 'F', 7777)

    # print(myGraph.getNexts('A'))
