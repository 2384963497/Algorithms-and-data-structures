# 实现栈
class Stack():
    def __init__(self) -> None:
        self.stack = []
    
    def pop(self):
        return self.stack.pop()
    
    def push(self, item):
        self.stack.append(item)
    
    def isEmpty(self):
        if len(self.stack) == 0:
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

    def DFS(self, begin):
        global searched, tempStack

        tempStack = Stack()
        searched = set()

        # 初始化
        tempVertex = self.getVertex(begin)
        
        searched.add(begin)
        self.DFSfunc(tempVertex)

        while not tempStack.isEmpty():
            print(f"{tempStack.pop()} - ", end = '')

    def DFSfunc(self, tempVertex):
        global searched, tempStack

        tempStack.push(tempVertex.item)

        for i in tempVertex.nexts:
            if i not in searched:
                searched.add(i)
                self.DFSfunc(self.getVertex(i))

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
    myGraph.DFS('D')

    












