# rt 

# 实现Node
class Node():
    def __init__(self):
        self.Pass = 0
        self.End = 0
        self.Nexts = dict()


# 实现Tree
class Trie():
    def __init__(self):
        self.root = Node()
    
    # 增
    def addStr(self, tStr):
        tempNode = self.root
        tempNode.Pass += 1

        if len(tStr) == 0:# 空串
            tempNode.End += 1
            return
        
        for i in range(len(tStr)):
            tempChar = tStr[i]
            if tempNode.Nexts.get(tempChar) ==  None:   # 是否tempChar对应的子节点
                tempNode.Nexts[tempChar] = Node()
                tempNode = tempNode.Nexts[tempChar]
            else:
                tempNode = tempNode.Nexts[tempChar]
            tempNode.Pass += 1

        tempNode.End += 1

    # 删
    def delStr(self, tStr):
        if not self.exist(tStr):    # 字符串不存在
            return None
        
        tempNode = self.root
        tempNode.Pass -= 1
        
        for i in range(len(tStr)):
            tChar = tStr[i]
            if tempNode.Nexts[tChar].Pass - 1 == 0:
                tempNode.Pass -= 1
                tempNode.Nexts.pop(tChar)
                return True
            else:
                tempNode = tempNode.Nexts[tChar]
                tempNode.Pass -= 1
        tempNode.End -= 1
        
            
                
        

    # 查询一个字符串是否在树上
    def exist(self, tStr):
        tempNode = self.root
        
        for i in range(len(tStr)):
            tChar = tStr[i]
            if tempNode.Nexts.get(tChar) == None:   # 没有以字符串tStr开头
                return False
            else:
                tempNode = tempNode.Nexts[tChar]

        if tempNode.End > 0:
            return True
        return False

    # 查询有多少个字符串是以str为前缀的
    def strCheck(self, tStr):
        tempNode = self.root
        
        for i in range(len(tStr)):
            tChar = tStr[i]
            if tempNode.Nexts.get(tChar) == None:   # 没有以字符串tStr开头
                return None
            else:
                tempNode = tempNode.Nexts[tChar]
        
        return tempNode.Pass

    # 查询有多少个字符串空串
    def getNull(self):
        return self.root.End

    # 返回前缀树上字符串的个数
    def getNum(self):
        return self.root.Pass



if __name__ == '__main__':
    myTrie = Trie()
    myTrie.addStr("apple")
    myTrie.addStr("CDC")
    myTrie.addStr("app")
    myTrie.addStr("aBp")
    myTrie.addStr("CSC")
    myTrie.addStr("awm")
    myTrie.addStr("apend")
    myTrie.addStr("CCTV")
    myTrie.addStr("我是靓仔")
    myTrie.addStr("ap伤害")
    myTrie.addStr("ap")
    myTrie.addStr("ap伤害")
    myTrie.addStr("")
    myTrie.addStr("我是帅哥")
    myTrie.addStr("你是靓仔")
    myTrie.addStr("")
    

    # tStr = 'ap'
    # count = myTrie.strCheck(tStr)
    # if count == None:
    #     print(f"没有以{tStr}开头的字符串！！！")
    # else:
    #     print(f"有{count}个以{tStr}开头的字符串")

    # 查询存在
    # print(myTrie.exist('我是'))

    # 删除
    print(myTrie.getNum())
    myTrie.delStr("")
    print(myTrie.getNum())

