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

    def MST(self):
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

    cost, result = myGraph.MST()

    print(f"MST的开销是{cost}")


