# rt

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

A = 5
B = 4
C = 2 
D = 2
E = 1
ex = 'ABCE*+*C*'
# ex = "AB*CD*-"
temp = Stack()

for i in ex:
    if i in '+-*//%':
        x = temp.pop()
        y = temp.pop()
        result = eval(y + i + x) #后面的操作数先出栈; 为了避免减法和除法顺序改变 写出 y i x
        temp.push(str(result))
    else:
        temp.push(i)
print(result)