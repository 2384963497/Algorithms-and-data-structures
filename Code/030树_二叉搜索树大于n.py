# 请写出递归算法，从小到大输出二叉排序树中所有数据值≥x的结点的数据。
# 要求先找到第一个满足条件的结点后，再依次输出其他满足条件的结点。

# Node类
class Node():
    def __init__(self, item):
        self.item = item
        self.lTree = None
        self.rTree = None


# BST类
class BST():
    def __init__(self):
        self.root = None

    def add(self, item):
        if self.root == None:
            tempNode = Node(item)
            self.root = tempNode
            return
        tempNode = self.root
        while tempNode != None:
            if item < tempNode.item:
                if tempNode.lTree == None:
                    tempNode.lTree = Node(item)
                    return
                tempNode = tempNode.lTree
            elif item > tempNode.item:
                if tempNode.rTree == None:
                    tempNode.rTree = Node(item)
                    return
                tempNode = tempNode.rTree
            else:
                print("The number has existed")
                return None

        

    def inOrder(self, node):
        if node == None:
            return None

        if node.lTree != None:
            self.inOrder(node.lTree)
        print(node.item)
        if node.rTree != None:
            self.inOrder(node.rTree)

    def func(self, key, node = False):
        global flag
        if self.root == None:
            return None
        if node == None:
            return

        if node == False:# 指定起始点
            node = self.root
        if node.lTree != None:
            self.func(key, node.lTree)
        if node.item >= key:
            flag = True
        if flag:
            print(node.item)
        if node.rTree != None:
            self.func(key, node.rTree)
        


if __name__ == '__main__':
    myBST = BST()
    myBST.add(100)
    myBST.add(75)
    myBST.add(110)
    myBST.add(50)
    myBST.add(80)
    myBST.add(120)
    myBST.add(115)
    myBST.add(130)
    myBST.add(125)
    myBST.add(126)
    myBST.add(123)

    x = int(input())
    flag = False
    myBST.func(x)


