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


result = Stack()
num = int(input("请输入需要转换的十进制数:"))

while num:
    result.push(num % 16)
    num //= 16

print("转换后为:")
while result.size():
    i = result.pop()
    if i<10:
        print(i, end = '')
    else:
        print(chr(65+i-10), end = '')


