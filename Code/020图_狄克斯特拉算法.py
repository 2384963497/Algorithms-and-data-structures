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
        self.vertexValue = []

    def addVertex(self, value):
        tempVertex = Vertex(value)
        self.vertexValue.append(value)
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

    def getVertex(self, value):
        '''
            通过所给value值 返回顶点的地址
        '''
        for i in self.vertexs:
            if i.value == value:
                return i

    def getVertexNum(self):
        return len(self.vertexValue)

    def Dij(self, begin):
        result = {}
        locked = []
        for i in self.vertexValue:  # 初始化  其余点到起点的距离都置为None
            result[i] = None
            if i == begin:          # 到自己的距离置为0
                result[i] = 0
        
        # 最开始定义一个变量指向出发点
        tempVertex = self.getVertex(begin)
        locked.append(tempVertex.value)

        while len(locked) < self.getVertexNum():
            minWeight = None
            minNext = None
            for i in tempVertex.nexts:
                if (minWeight == None or minWeight > tempVertex.nexts[i]) and i not in locked:
                    minNext = i
                    minWeight = tempVertex.nexts[i]
                if result[i] == None or result[i] > result[tempVertex.value] + tempVertex.nexts[i]:
                    result[i] = result[tempVertex.value] + tempVertex.nexts[i]
            
            # 选择一条权值最小的路径 继续以上操作
            tempVertex = self.getVertex(minNext)
            locked.append(tempVertex.value)

        

        return result


if __name__ == '__main__':
    myGraph = Graph()
    myGraph.addVertex('A')
    myGraph.addVertex('B')
    myGraph.addVertex('C')
    myGraph.addVertex('D')
    myGraph.addVertex('E')
    myGraph.addVertex('F')
    myGraph.addEdge('A', 'B', 3)
    myGraph.addEdge('A', 'C', 19)
    myGraph.addEdge('A', 'D', 9)
    myGraph.addEdge('C', 'D', 7)
    myGraph.addEdge('C', 'B', 12)
    myGraph.addEdge('C', 'E', 14)
    myGraph.addEdge('E', 'F', 7777)
    myGraph.addEdge('E', 'B', 200)
    myGraph.addEdge('E', 'D', 20)


    result = myGraph.Dij('A')
    for i in result:
        print(f"A点到{i}的最短距离为{result[i]}")
    print("-"*30)
    result = myGraph.Dij('C')
    for i in result:
        print(f"C点到{i}的最短距离为{result[i]}")
    # print(myGraph.getNexts('A'))