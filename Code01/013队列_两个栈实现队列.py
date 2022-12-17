# rt

class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)

class Queue():
    def __init__(self):
        self.inPut = Stack()
        self.outPut = Stack()
    
    def size(self):
        return len(self.inPut) + len(self.outPut)
    
    def enqueue(self, item):
        self.inPut.push(item)
    
    def dequeue(self):
        if self.outPut.size() == 0:
            if self.inPut.size() == 0:
                print("队列为空,不能出队！！")
                return None
            else:
                while self.inPut.size():
                    self.outPut.push(self.inPut.pop())
        
        return self.outPut.pop()

temp = Queue()
temp.enqueue(1)
temp.enqueue(2)
temp.enqueue(3)
print(temp.dequeue())
print(temp.dequeue())
temp.enqueue(3)
temp.enqueue(4)
print(temp.dequeue())
print(temp.dequeue())
print(temp.dequeue())
print(temp.dequeue())



