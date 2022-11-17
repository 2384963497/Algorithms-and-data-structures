# 比较器
def cmp(a, b):
    if a.Weight > b.Weight:
        return True
    return False

# 堆排序
def heapSort(List):
    # heapInsert  升序  创建大根堆
    for i in range(len(List)):
        j = i
        while j > 0 and cmp(List[j], List[(j-1)//2]):
            List[j], List[(j-1)//2] = List[(j-1)//2], List[j]
            j = (j-1)//2
    
    # 开始排序
    deep = len(List)-1
    while deep > 0 :
        List[deep], List[0] = List[0], List[deep]
        deep -= 1
        
        # heapify
        i = 0
        j = 2*i+1
        while j <= deep:
            if j+1 <= deep and cmp(List[j+1], List[j]):
                j = j+1

            if cmp(List[i], List[j]):
                break
            else:
                List[i], List[j] = List[j], List[i]
                i = j
                j = 2*i+1
# 实现Vertex
class Vertex():
    def __init__(self, item):
        self.item = item

# 实现Edge
class Edge():
    def __init__(self, From, To, Weight):
        self.From = From
        self.To = To
        self.Weight = Weight

# 实现Graph
class Graph():
    def __init__(self):
        self.vertexs = []
        self.edges = []
        self.vSize = 0

    def addVertex(self, item):
        tempVertex = Vertex(item)
        self.vertexs.append(tempVertex)
        self.vSize += 1

    def addEdge(self, From, To, Weight):
        tempEdge = Edge(From, To, Weight)
        self.edges.append(tempEdge)
    
    def getVertex(self, item):
        for i in self.vertexs:
            if i.item == item:
                return i

    def P_MST(self):
        doneSet = set()
        unsettleSet = set()
        cost = 0
        result = []
        # doneEdge = []
        # 1.指定一个起始点, 将该点所发散的边解锁；将点加入已处理点合
        unsettleSet = {i for i in self.vertexs}
        curVertex = self.vertexs[0]
        
        myHeap = []
        
        doneSet.add(curVertex)
        unsettleSet.remove(curVertex)   
        
        while len(unsettleSet):
            for i in self.edges:
                if (i.From == curVertex.item or i.To == curVertex.item) \
                    and \
                    (self.getVertex(i.From) not in doneSet or self.getVertex(i.To) not in doneSet):  
                    # 解锁已处理点所以关联的边;  至少有一边的点没有处理过
                    myHeap.append(i)
                    heapSort(myHeap)

            
            # 选择一个合法的边处理
            while True:
                tempEdge = myHeap.pop(0)
                if self.getVertex(tempEdge.From) not in doneSet:
                    cost += tempEdge.Weight
                    result.append(tempEdge)
                    curVertex = self.getVertex(tempEdge.From)
                    doneSet.add(curVertex)
                    unsettleSet.remove(curVertex)
                    break
                elif self.getVertex(tempEdge.To) not in doneSet:
                    cost += tempEdge.Weight
                    result.append(tempEdge)
                    curVertex = self.getVertex(tempEdge.To)
                    doneSet.add(curVertex)
                    unsettleSet.remove(curVertex)
                    break
        return cost, result
    
    def K_MST(self):
    # 为每个节点都建立一个集合
        sets = []
        result = []
        cost = 0
        for i in self.vertexs:
            sets.append({i})
        # 边排序
        heapSort(self.edges)
        for tempEdge in self.edges:
            From = self.getVertex(tempEdge.From)
            To = self.getVertex(tempEdge.To)
            # 找到两个点的所在集合
            for i in sets:
                if From in i:
                    a = i
                if To in i:
                    b = i
            if a == b:
                continue
            else:
                a |= b
                sets.remove(b)
                result.append(tempEdge)
                cost += tempEdge.Weight
            if len(sets) == 1:
                break

        return cost, result


if __name__ == '__main__':
    myGraph = Graph()
    myGraph.addVertex('A')
    myGraph.addVertex('B')
    myGraph.addVertex('C')
    myGraph.addVertex('D')
    myGraph.addVertex('E')
    myGraph.addVertex('F')
    myGraph.addVertex('G')
    
    myGraph.addEdge('A', 'B', 11)
    myGraph.addEdge('A', 'C', 6)
    myGraph.addEdge('A', 'D', 5)
    myGraph.addEdge('B', 'C', 7)
    myGraph.addEdge('C', 'D', 12)
    myGraph.addEdge('B', 'E', 4)
    myGraph.addEdge('B', 'F', 9)
    myGraph.addEdge('C', 'F', 2)
    myGraph.addEdge('D', 'F', 1)
    myGraph.addEdge('E', 'F', 8)
    myGraph.addEdge('G', 'F', 10)
    myGraph.addEdge('D', 'G', 3)

    cost1, result1 = myGraph.P_MST()
    cost2, result2 = myGraph.K_MST()


    print(set(result1) == set(result2))


