
class loopQueue():
    def __init__(self, Length):
        self.maxLength = Length
        self.queue  = [None] * self.maxLength
        self.rear = self.front = 0
    
    def isEmpty(self):
        if self.rear == self.front:
            return True
        return False
    
    def isFull(self):
        if (self.rear + 1) % self.maxLength == self.front:
            return True
        return False

    def enqueue(self, data):
        if self.isFull():
            print("队已满！禁止入队！！")
            return None
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.maxLength
    
    def dequeue(self):
        if self.isEmpty():
            print("队为空！禁止出队！！！")
            return None
        temp =  self.queue[self.front]
        # self.queue[self.front] = None
        self.front = (self.front + 1) % self.maxLength
        return temp
        
    def size(self):
        if self.rear >= self.front:
            return self.rear - self.front
        else:
            return self.maxLength - self.front + self.rear

myqueue = loopQueue(6)
print(myqueue.size())
myqueue.enqueue(1)
myqueue.enqueue(2)
print(myqueue.size())
myqueue.enqueue(3)
myqueue.enqueue(4)
myqueue.enqueue(5)
print(myqueue.size())
myqueue.dequeue()
myqueue.dequeue()
myqueue.dequeue()
myqueue.dequeue()
myqueue.dequeue()
print(myqueue.size())
myqueue.enqueue(6)
myqueue.enqueue(7)
myqueue.enqueue(8)
myqueue.enqueue(9)
print(myqueue.size())
# myqueue.enqueue(6)
