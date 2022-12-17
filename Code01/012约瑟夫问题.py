# 传说犹太人反叛罗马人，落到困境，约瑟夫和39人决定殉难，坐成一圈儿(1~40)，报数1～7，
# 报到7的人由旁边杀死，结果约瑟夫给自己安排了个位置，最后他自己存活了下来；
# 求他的起始位置

class queue():
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

q = queue()
q.items = [ i for i in range(40, 0, -1)] #生成队列
print(q)

while q.size()>1:
    for i in range(1, 8):
        if i != 7:
            q.enqueue(q.dequeue())
        else:
            del q.items[-1]
            print(q)

print(q)
