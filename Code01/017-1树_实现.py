# rt

from collections import deque

# 定义节点类
class Node():
    def __init__(self, data):
        self.data = data
        self.lnode = None
        self.rnode = None

class bTree():
    def __init__(self):
        self.root = None
        self.size = 0
    
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    
    def numNodes(self):
        return self.size
    
    def add(self, data):
        tempNode = Node(data)
        if self.size == 0:
            self.root = tempNode
            self.size += 1 
            return 
        tempQueue = deque()
        tempQueue.append(self.root)
        while True:
            temp = tempQueue.popleft()
            if temp.lnode == None:
                temp.lnode = tempNode
                self.size += 1
                break
            elif temp.rnode == None:
                temp.rnode = tempNode
                self.size += 1
                break
            else:
                tempQueue.append(temp.lnode)
                tempQueue.append(temp.rnode)
    
    # 层次遍历
    def travel(self):
        if self.size == 0:
            return None
        tempQueue = deque()
        tempQueue.append(self.root)
        while tempQueue.__len__() > 0:
            temp = tempQueue.popleft()
            print(temp.data, end = ' ')
            if temp.lnode != None:
                tempQueue.append(temp.lnode)
            if temp.rnode != None:
                tempQueue.append(temp.rnode)

    # 先序遍历
    def preOrder(self):
        if self.size == 0:
            return
        self.preOrderFunc(self.root)

    def preOrderFunc(self, node):
        if node == None:
            return
        print(node.data, end = ' ')
        self.preOrderFunc(node.lnode)
        self.preOrderFunc(node.rnode)

    # 中序遍历
    def inOrder(self):
        if self.size == 0:
            return
        self.inOrderFunc(self.root)

    def inOrderFunc(self, node):
        if node == None:
            return
        self.inOrderFunc(node.lnode)
        print(node.data, end = ' ')
        self.inOrderFunc(node.rnode)
    
    # 后序遍历
    def postOrder(self):
        if self.size == 0:
            return
        self.postOrderFunc(self.root)

    def postOrderFunc(self, node):
        if node == None:
            return
        self.postOrderFunc(node.lnode)
        self.postOrderFunc(node.rnode)
        print(node.data, end = ' ')
    

if __name__ == '__main__':
    mybTree = bTree()

    mybTree.add(0)
    mybTree.add(1)
    mybTree.add(2)
    mybTree.add(3)
    mybTree.add(4)
    mybTree.add(5)
    mybTree.add(6)
    mybTree.add(7)
    mybTree.add(8)
    mybTree.add(9)

    print(mybTree.size)
    print("\n")
    mybTree.preOrder()
    print("\n")
    mybTree.inOrder()
    print("\n")
    mybTree.postOrder()




