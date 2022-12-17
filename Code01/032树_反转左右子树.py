# 翻转整棵树的所有左右子树

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
            return
        
        self.inOrder(node.lTree)
        print(node.item)
        self.inOrder(node.rTree)

    def func(self, node):
        if node == None:
            return
        node.lTree, node.rTree = node.rTree, node.lTree
        self.func(node.lTree)
        self.func(node.rTree)
            
        
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

    myBST.inOrder(myBST.root)
    myBST.func(myBST.root)
    print("翻转后为:")
    myBST.inOrder(myBST.root)
    