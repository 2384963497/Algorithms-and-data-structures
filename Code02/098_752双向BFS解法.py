
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

l1 = ['0000']
l2 = [target]
visited = set(deadends)
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

while l1 and l2:
    temp = []
    
    # 拓展l1将有效后续放入temp中
    for i in l1:
        if i in l2:
            # return count
            print(count)
        for j in range(4):
            t = upNum(i, j)
            if t not in visited:
                temp.append(t)
            t = downNum(i, j)
            if t not in visited:
                temp.append(t)
        visited.add(i)

    count += 1
    l1 = l2
    l2 = temp

    






