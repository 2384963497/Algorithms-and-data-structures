from queue import Queue

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

used = set(deadends)
q = Queue()
count = 0

def upNum(s, i):
    s = list(s)
    s[i] = chr(ord(s[i]) + 1)
    if s[i] > '9':
        s[i] = '0'
    return ''.join(s)

def downNum(s, i):
    s = list(s)
    s[i] = chr(ord(s[i]) - 1)
    if s[i] < '0':
        s[i] = '9'
    return ''.join(s)

q.put('0000')

while not q.empty():
    i = q._qsize()

    while i > 0:
        cur = q.get()
        if cur == target:
            print(count)
        # 处理当层的节点
        for j in range(0, 4):
            # 每个节点有8个子节点
            temp = upNum(cur, j)
            if temp  not in used:
                q.put(temp)
                used.add(temp)
            temp = downNum(cur, j)
            if temp  not in used:
                q.put(temp)
                used.add(temp)
        i -= 1
    count += 1
print(-1)
    


    
