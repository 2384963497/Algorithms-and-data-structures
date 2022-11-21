# 求一颗搜索二叉树的宽度 
# 树结构


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

    def func(self, node):
        if node == None:
            return 0
        
        tQueue = []
        ln = 1
        tQueue.append([node, ln])
        i = 0
        
        while True:
            if tQueue[i][0].lTree != None:
                tQueue.append([tQueue[i][0].lTree, tQueue[i][1] + 1])
            if tQueue[i][0].rTree != None:
                tQueue.append([tQueue[i][0].rTree, tQueue[i][1] + 1])
            i += 1
            if i == len(tQueue):
                break
        
        r = dict()
        for i in tQueue:
            if i[1] not in r:
                r[i[1]] = 1
            else:
                r[i[1]] += 1
        max = 0
        for i in r:
            if r[i] > max:
                max = r[i]
        return max
if __name__ == '__main__':
    myBST = BST()
    myBST.add(100)
    myBST.add(75)
    myBST.add(110)
    myBST.add(50)
    myBST.add(80)
    myBST.add(120)
    myBST.add(115)
    myBST.add(105)
    myBST.add(130)
    myBST.add(125)
    myBST.add(126)
    myBST.add(123)


    width = myBST.func(myBST.root)
    print(f"这颗二叉树的深度为{width}")
    