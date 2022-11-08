# rt


class Node():
    
    def __init__(self, item):
        self.item = item
        self.next = None
    

class linkList():
    
    def __init__(self, node=None):
        self._head = node
    
    def isEmpty(self):
        if self._head == None:
            return True
        return False
    
    def add(self, item):
        tempNode = Node(item)
        tempNode.next = self._head
        self._head = tempNode

    def length(self):
        curr = self._head
        l=0
        while curr != None:
            l+=1
            curr = curr.next
        return l
    
    def travel(self):
        curr = self._head
        while curr != None:
            print(curr.item, end='    ')
            curr = curr.next

    def append(self, item):
        tempNode = Node(item)
        if self.isEmpty():
            self._head = tempNode
        else:
            curr = self._head
            while curr.next != None:
                curr = curr.next
            curr.next = tempNode

    def search(self, key):
        curr = self._head
        while curr!= None and curr.item != key:
            curr = curr.next
        if curr == None:
            return False
        return True

    def remove(self, key):
        if self.search(key):
            curr = self._head
            pre = curr
            while curr != None and curr.item != key:
                pre = curr
                curr = curr.next
            if curr == self._head:   # 移除首个元素
                self._head = curr.next
            else:
                pre.next = curr.next
        else:
            print("无该元素！")
            return None

    def insert(self, pos, item):
        if pos >= self.length():
            self.append(item)
        elif pos <= 0:
            self.add(item)
        else:
            pre = self._head
            i = 0
            while i < pos-1:
                pre = pre.next
                i+=1
            tempNode = Node(item)
            tempNode.next = pre.next
            pre.next = tempNode
        

            


        
myLink = linkList()
myLink.add(100)
myLink.append(700)
myLink.append(600)
myLink.append('hello')
myLink.append('wrold')
myLink.append("last")
myLink.travel()
myLink.remove(100)
myLink.remove('hello')
print("\n")
myLink.travel()
# myLink.insert(4, 'Flag')
# print("\n")
# myLink.travel()
