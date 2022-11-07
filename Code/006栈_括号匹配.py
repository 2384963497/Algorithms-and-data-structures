#输入一个字符串;判断其中的括号是否成对是否合法
#合法输出NICE!  非法输出ERROR!
#(1+6*(2+3(a+c)),O(n*long(n*(2+6(a+c)))))     NICE!
#(1+6*(2+3(a+c)),{O(n*long(n*([2+6(a+c)])))})     NICE!
#(1+6*[(2+3(a+c])),O(n*long(n*([2+6(a+c)]))))     ERROR!

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

temp = Stack()
sTemp = input("请输入需要检验的字符串:")

fTemp = True
for i in sTemp:
    if i in '([{':
        temp.push(i)
    if i == ')':
        if temp.peek() == '(':
            temp.pop()
        else:
            fTemp = False
            break
    if i == ']':
        if temp.peek() == '[':
            temp.pop()
        else:
            fTemp = False
            break
    if i == '}':
        if temp.peek() == '{':
            temp.pop()
        else:
            fTemp = False
            break

if temp.size():
    fTemp = False

if fTemp:
    print("NICE!")
else:
    print("ERROR!")
