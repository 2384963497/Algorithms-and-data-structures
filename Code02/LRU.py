class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.last = None
        self.next = None

class doubleLink():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, node):
        if self.head == None:
            # 当前为空链表
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.last = self.tail
            self.tail = self.tail.next

    def remove(self, node):
        if self.head == self.tail:
            # 删除唯一节点
            self.head = None
            self.next = None
        elif node.last == None:
            # 删除头节点
            self.head = node.next
            node.next.last = None
        elif node.next == None:
            # 删除尾节点
            self.tail = node.last
            node.last.next = None
        else:
            # 普遍节点
            node.next.last = node.last
            node.last.next = node.next

class LRUCache:

    def __init__(self, capacity: int):
        self.MAX = capacity
        self.len = 0
        self.Map = dict()
        self.link = doubleLink()


    def get(self, key: int) -> int:
        res = self.Map.get(key)
        if res == None:
            return -1
        # 访问有效值要更新相对位置
        self.link.remove(res)
        self.link.append(res)

    def put(self, key: int, value: int) -> None:
        tempNode = Node(key, value)
        if self.Map.get(key) != None:
            # key已经存在
            self.link.remove(self.Map[key])
            self.Map.pop(key)
            self.len -= 1
        # 追加
        self.link.append(tempNode)
        self.Map[key] = tempNode
        self.len += 1
        if self.len > self.MAX:
            self.Map.pop(self.link.head.key)
            self.link.remove(self.link.head)
            self.len -= 1
obj = LRUCache(3)
obj.put(1, 1)
obj.put(2, 2)
obj.put(3, 3)
obj.get(1)
obj.put(4, 4)
obj.put(5, 5)
