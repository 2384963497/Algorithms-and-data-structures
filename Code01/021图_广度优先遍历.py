# 实现队列
class Queue():
    def __init__(self):
        self.quque = []

    def push(self, item):
        self.quque.append(item)

    def pop(self):
        return self.quque.pop(0)
    
    def isEmpty(self):
        if len(self.quque) == 0:
            return True
        else:
            return False
# Vertex类的定义
class Vertex():
    def __init__(self, item):
        self.item = item
        self.nexts = {}
    
    def addEdge(self, To, weight = None):
        self.nexts[To] = weight
# Graph类的定义
class Graph():
    def __init__(self):
        self.vertexs = []
        self.len = 0
    
    def addVertex(self, item):
        tempVertex = Vertex(item)
        self.vertexs.append(tempVertex)
        self.len += 1
    
    def addEdge(self, From, To, weight = None):
        for i in self.vertexs:
            if i.item == From:
                i.addEdge(To, weight)
            if i.item == To:
                i.addEdge(From, weight)
    
    def getVertex(self, item):
        for i in self.vertexs:
            if i.item == item:
                return i

    def BFS(self, begin):
        tempQueue = Queue()
        searched = set()
        unSearched = set()
        

        # 指定遍历起始点
        for i in self.vertexs:
            unSearched.add(i.item)
            if i.item == begin:
                tempVertex = i

        tempQueue.push(tempVertex)
        while not tempQueue.isEmpty():
            tempVertex = tempQueue.pop()
            print(tempVertex.item, end = ' - ')
            for i in tempVertex.nexts:
                if i not in searched:
                    searched.add(i)
                    unSearched.remove(i)
                    tempQueue.push(self.getVertex(i))
       

if __name__ == '__main__':
    myGraph = Graph()
    myGraph.addVertex("A")
    myGraph.addVertex("B")
    myGraph.addVertex("C")
    myGraph.addVertex("D")
    myGraph.addVertex("E")
    myGraph.addVertex("F")
    myGraph.addVertex("G")
    myGraph.addVertex("H")

    myGraph.addEdge('A', 'B')
    myGraph.addEdge('A', 'E')
    myGraph.addEdge('B', 'C')
    myGraph.addEdge('B', 'D')
    myGraph.addEdge('C', 'D')
    myGraph.addEdge('C', 'G')
    myGraph.addEdge('C', 'F')
    myGraph.addEdge('G', 'F')
    myGraph.addEdge('E', 'H')

    # 广度优先遍历
    myGraph.BFS('F')














