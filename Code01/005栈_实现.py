# 用python中的列表来实现栈

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

myFirst = Stack()

print(myFirst.peek())
print(myFirst.isEmpty())
print(myFirst.size())
myFirst.push('(')
myFirst.push('你好')
myFirst.push(')')
myFirst.push('芜湖~~~')
print(myFirst)
myFirst.pop()
print(myFirst)
