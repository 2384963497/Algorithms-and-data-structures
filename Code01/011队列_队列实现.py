# rt
class queue():
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    



