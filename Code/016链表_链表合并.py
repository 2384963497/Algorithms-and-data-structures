# 两个有序链表和并; 要求合并后的新链表已然有序
# [1, 3, 5, 7, 9, 11 ,15]
# [0, 2, 4, 6, 8, 9, 10, 12, 777, 4396]
class Node():
    
    def __init__(self, item):
        self.item = item
        self.next = None
    

class linkList():
    
    def __init__(self, node = None):
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
            pre = curr = self._head
            while curr.next != None and curr.item != key:
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
    
    def reverse(self):
        if self.length() <= 1:
            return
        pre = curr = self._head
        temp = curr.next
        curr.next = None
        curr = temp
        while temp != None:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        self._head = pre
# 链表实现

def mergeList(la, lb):
    lc = linkList()
    # 判断是否有空链表  略
    pa = la._head
    pb = lb._head
    if pa.item <= pb.item:
        lc._head = pa
        pa = pa.next
    else:
        lc._head = pb
        pb = pb.next
    
    tail = lc._head
    while pa != None and pb != None:
        if pa.item <= pb.item:
            tail.next = pa
            tail = tail.next
            pa = pa.next
        else:
            tail.next = pb
            tail = tail.next
            pb = pb.next
    if pa == None:
        tail.next = pb
    if pb == None:
        tail.next = pa

    return lc


la = linkList()
la.append(1)
la.append(3)
la.append(5)
la.append(7)
la.append(9)
la.append(11)
la.append(15)
lb = linkList()
lb.append(0)
lb.append(2)
lb.append(4)
lb.append(6)
lb.append(8)
lb.append(9)
lb.append(10)
lb.append(12)
lb.append(777)
lb.append(4396)

lc = mergeList(la, lb)
lc.travel()