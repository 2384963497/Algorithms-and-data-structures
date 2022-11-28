
n = 4
res = []

def isValid(depth, y, path):
    for i in range(len(path)):
        if path[i] == y or abs(depth - i) == abs(y - path[i]):
            return False
    return True

def DFS(depth, path):
    if len(path) == n:
        temp = [['.'] * n for i in range(n)]
        for i in range(n):
            temp[i][path[i]] = 'Q'
        res.append([''.join(t) for t in temp])
        return

    for j in range(n):
        if isValid(depth, j, path):
            path.append(j)
            DFS(depth + 1, path)
            path.pop()

DFS(0, [])
print(res)


