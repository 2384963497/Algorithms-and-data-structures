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

temp = Stack()
exp = input("请输入对应表达式(空格分隔):").split(' ')
for i in exp:
    if i == '(':
        temp.push(i)
        continue

    if i == ')':
        while temp.peek() != '(':
            print(temp.pop(), end='')
        temp.pop()
        continue

    if i in '+-*//%':
        if temp.size() == 0 or temp.peek() == '(':  #
            temp.push(i)
        elif i in '*//%' and temp.peek() in '+-':  # 优先级高于栈顶
            temp.push(i)
        else:   # 优先级低于栈顶 或 等于栈顶
            print(temp.pop(), end='')
            temp.push(i)
    else:
        print(i, end = '')
while temp.size():
    i = temp.pop()
    print(i, end = '')

# A * ( B - C * E ) * C
# A * B + C * D