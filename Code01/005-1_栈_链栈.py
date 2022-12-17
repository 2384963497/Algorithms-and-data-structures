# 表达式括号匹配
# (1+6*(2+3(a+c)),O(n*long(n*(2+6(a+c)))))     NICE!
# (1+6*(2+3(a+c)),{O(n*long(n*([2+6(a+c)])))})     NICE!
# (1+6*[(2+3(a+c])),O(n*long(n*([2+6(a+c)]))))     ERROR!

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkStack():
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        if self.top == None:
            return True
        return False

    def push(self, data):
        tempNode = Node(data)
        tempNode.next = self.top
        self.top = tempNode
    
    def pop(self):
        if self.isEmpty():
            return None
        temp = self.top.data
        self.top = self.top.next
        return temp

    def travel(self):
        if self.isEmpty():
            print("链栈为空！！！")
            return 
        tempTop = self.top
        while tempTop != None:
            print(tempTop.data, end = '')
            tempTop = tempTop.next

myLinckStack = linkStack()

lBracket = ['{', '[', '(']
rBracket = ['}', ']', ')']

ex = input("请输入表达式:")
flag = True
for ch in ex:
    if ch in lBracket:
        myLinckStack.push(ch)
    elif ch in rBracket:
        if lBracket.index(myLinckStack.pop()) != rBracket.index(ch):
            flag = False
            break
if not myLinckStack.isEmpty():
    flag = False
if flag:
    print("Match!")
else:
    print("Mismatch!!!!!")
