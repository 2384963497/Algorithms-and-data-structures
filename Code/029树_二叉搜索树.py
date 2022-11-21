# 二叉搜索树的实现

# 定义Node类
class Node():
    def __init__(self, item):
        self.item = item
        self.lTree = None
        self.rTree = None
        self.pNode = None

# 定义BST类
class BST():
    # 初始化
    def __init__(self):
        self.root = None
    
    # 中序遍历
    def inOrder(self, node):
        if node == None:
            return
        
        self.inOrder(node.lTree)
        print(node.item)
        self.inOrder(node.rTree)
        
    # 增
    def add1(self, item):
        # 非递归调用
        if self.root == None:
            self.root = Node(item)
            return
        tempNode = self.root
        while tempNode != None:
            if item < tempNode.item:
                if tempNode.lTree == None:
                    tempNode.lTree = Node(item)
                    tempNode.lTree.pNode = tempNode
                    return
                else:
                    tempNode = tempNode.lTree
            elif item > tempNode.item:
                if tempNode.rTree == None:
                    tempNode.rTree = Node(item)
                    tempNode.rTree.pNode = tempNode
                    return
                else:
                    tempNode = tempNode.rTree
            else:
                print("The num has been pushed!")

    def add(self, node, item):# 递归调用
        if self.root == None:
            tempNode = Node(item)
            self.root = tempNode
            return

        if node == None:
            node = Node(item)
            return node
        elif item < node.item:
            r = self.add(node.lTree, item)
            if r != None:
                r.pNode = node
                node.lTree = r
        elif item > node.item:
            r = self.add(node.rTree, item)
            if r != None:
                r.pNode = node
                node.rTree = r
        else:
            print("The number has been pushed!")
        return None


    # 删
    # 分类讨论删除节点的孩子情况
    # 一个孩子
    # 两个孩子
    # 没有孩子
    def Del(self, item):
        r = self.search1(item)
        # 判断数中是否有该数
        if r == None:
            return None
        
        if r.lTree == None and r.rTree == None:
            if r.item < r.pNode.item:   # 删除节点为父节点的左子树
                r.pNode.lTree = None
            else:
                r.pNode.rTree = None
        elif r.lTree == None and r.rTree != None:   # 只有右子树
            if r.pNode == None: # 删除的是根节点
                self.root = r.rTree
                r.rTree.pNode = None
                return item
            r.rTree.pNode = r.pNode
            if r.item < r.pNode.item:
                r.pNode.lTree = r.rTree
            else:
                r.pNode.rTree = r.rTree
        elif r.lTree != None and r.rTree == None:   # 只有左子树
            if r.pNode == None: # 删除的是根节点
                self.root = r.lTree
                r.lTree.pNode = None
                return item
            r.lTree.pNode = r.pNode
            if r.item < r.pNode.item:
                r.pNode.lTree = r.lTree
            else:
                r.pNode.rTree = r.lTree
        else:   # 拥有左右子树
            rMax = self.getmin(r.rTree)
            temp = rMax.item
            self.Del(temp)
            r.item = temp

             
    # 查
    def search(self, node ,key):
        # 递归
        if node == None:
            return None
        
        if key < node.item:
            return self.search(node.lTree, key)
        elif key > node.item:
            return self.search(node.rTree, key)
        else:
            return key
    
    def search1(self, key):
        # 非递归
        tempNode = self.root
        while tempNode != None:
            if key < tempNode.item:
                tempNode  = tempNode.lTree
            elif key > tempNode.item:
                tempNode  = tempNode.rTree
            else:
                return tempNode
        return None

    # 返回一棵树最大值和最小值节点
    def getMax(self, node):
        if self.root == None:
            return None
        tempNode = node
        while tempNode.rTree != None:
            tempNode = tempNode.rTree
        return tempNode

    def getmin(self, node):
        if self.root == None:
            return None
        tempNode = node
        while tempNode.lTree != None:
            tempNode = tempNode.lTree
        return tempNode

    # 改




if __name__ == '__main__':
    myBST = BST()
    myBST.add1(100)
    myBST.add1(75)
    myBST.add1(110)
    myBST.add1(50)
    myBST.add1(80)
    myBST.add1(120)
    myBST.add1(115)
    myBST.add1(130)
    myBST.add1(125)
    myBST.add1(126)
    myBST.add1(123)

    # myBST.add(myBST.root,100)
    # myBST.add(myBST.root,75)
    # myBST.add(myBST.root,110)
    # myBST.add(myBST.root,80)
    # myBST.add(myBST.root,50)


    # if myBST.search1(100):
    #     print("数中有该数字")
    # else:
    #     print("数中不存在这个数字")

    # print("---")
    # print(myBST.getMax(myBST.root).item)
    # print(myBST.getmin(myBST.root).item)

    print("-"*30)
    myBST.inOrder(myBST.root)

    myBST.Del(100)

    print("-"*30)
    myBST.inOrder(myBST.root)
    