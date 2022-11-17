from collections import deque

# Vertex实现
class Vertex():
    def __init__(self, item):
        self.item = item
        self.toNexts = []
        self.indegree = 0

    def addEdge(self, To):
        self.toNexts.append(To)
    
    def addIndegree(self):  
        self.indegree += 1

# Graph实现
class Graph():
    def __init__(self):
        self.vertexs = []
    
    def addVertex(self, item):
        tempVertex = Vertex(item)
        self.vertexs.append(tempVertex)
    
    def addEdge(self, From, To):
        for i in self.vertexs:
            if i.item == From:
                i.addEdge(To)
            if i.item == To:
                i.addIndegree()

    def getVertex(self, item):
        for i in self.vertexs:
            if i.item == item:
                return i

    def topoSort(self):
        result = deque()
        tempList = []
        for i in self.vertexs:
            tempList.append([i, i.indegree])
        
        print(tempList)
        while len(tempList) != 0:
            for i in tempList:
                if i[1] == 0:     # 找到剩下列表中入度为0的点
                    result.append(i[0])    # 把该点入队
                    for x in i[0].toNexts:# 擦除该点的影响
                        for j in tempList:
                            if x == j[0].item:
                                j[1] -= 1 
                    tempList.remove(i)
                    continue
        return result     
            
        
        
    

if __name__ == '__main__':
    myGraph = Graph()
    
    # 添加节点
    myGraph.addVertex("math.py")
    myGraph.addVertex("tool.py")
    myGraph.addVertex("string.py")
    myGraph.addVertex("path.py")
    myGraph.addVertex("time.py")
    myGraph.addVertex("main.py")

    # 添加边
    myGraph.addEdge("math.py", 'tool.py')
    myGraph.addEdge("time.py", "math.py")
    myGraph.addEdge("time.py", "path.py")
    myGraph.addEdge("time.py", "string.py")
    myGraph.addEdge("string.py", "math.py")
    myGraph.addEdge("path.py", "math.py")
    myGraph.addEdge("path.py", "string.py")
    myGraph.addEdge("math.py", "main.py")
    myGraph.addEdge("tool.py", "main.py")
    myGraph.addEdge("string.py", "main.py")


    result = myGraph.topoSort()
    print("文件的编译顺序为: ", end = '')
    while len(result) != 0:
        print(f" {result.popleft().item} ", end = '->')

















