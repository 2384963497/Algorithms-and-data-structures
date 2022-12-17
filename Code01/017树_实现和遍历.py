# rt
from collections import deque
# 内置队列
class Stack():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if self.size() == 0:
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
# 栈实现

class Node():
    def __init__(self,item):
        self.item = item
        self.lnode = None
        self.rnode = None
class biTree():
    def __init__(self):
        self.root = None
    
    def add(self, item):
        tempNode = Node(item)
        if self.root == None:   # 空树
            self.root = tempNode
            return
        tempQueue = deque()
        tempQueue.append(self.root)
        while True:
            temp = tempQueue.popleft()
            if temp.lnode == None:
                temp.lnode = tempNode
                break
            elif temp.rnode == None:
                temp.rnode = tempNode
                break
            else:
                tempQueue.append(temp.lnode)
                tempQueue.append(temp.rnode)
    
    # 层次遍历
    def breadth_travel(self):
        if self.root == None:
            print("树为空！！！")
            return 0
        tempQueue = deque()
        tempQueue.append(self.root)
        while tempQueue.__len__() > 0:
            temp = tempQueue.popleft()
            print(temp.item, end = '')
            if temp.lnode != None:
                tempQueue.append(temp.lnode)
            if temp.rnode != None:
                tempQueue.append(temp.rnode)

    # inorder 中序遍历
    def inorder_travel(self):
        if self.root == None:
            print("树为空！！！")
            return
        self.inorderFunc(self.root)
    def inorderFunc(self, node):
        if node == None:
            return
        self.inorderFunc(node.lnode)
        print(node.item, end = '')
        self.inorderFunc(node.rnode)
        
    # preorder 前序遍历
    def preorder_travel(self):
        if self.root == None:
            print("树为空！！！")
            return
        self.preorderFunc(self.root)

    def preorderFunc(self, node):
        if node == None:
            return
        print(node.item, end = '')
        self.preorderFunc(node.lnode)
        self.preorderFunc(node.rnode)



    # postorder 后序遍历
    def postorder_travel(self):
        if self.root == None:
            print("树为空！！！")
            return
        self.postorderFunc(self.root)
    def postorderFunc(self, node):
        if node == None:
            return
        self.postorderFunc(node.lnode)
        self.postorderFunc(node.rnode)
        print(node.item, end = '')

    def size(self):
        if self.root == None:
            return 0
        count = 0
        tempQueue = deque()
        tempQueue.append(self.root)
        while tempQueue.__len__() > 0:
            temp = tempQueue.popleft()
            count += 1
            if temp.lnode != None:
                tempQueue.append(temp.lnode)
            if temp.rnode != None:
                tempQueue.append(temp.rnode)
        return count
    

myTree = biTree()
myTree.add(0)
myTree.add(1)
myTree.add(2)
myTree.add(3)
myTree.add(4)
myTree.add(5)
myTree.add(6)
myTree.add(7)
myTree.add(8)
myTree.add(9)
#  myTree.add(11)
#  myTree.add(12)
#  myTree.add(13)
print("\n层次遍历:")
myTree.breadth_travel()
print("\n前序遍历:")
myTree.preorder_travel()
print("\n中序遍历:")
myTree.inorder_travel()
print("\n后续遍历:")
myTree.postorder_travel()
