
n = 4
res = []
def isValid(x, y, path):
    if path == []:
        return True
    for i in path:
        if i[1] == y:
            return False
    for i in path:
        if abs(i[0] - x) == abs(i[1] - y):
            return False
    return True


def DFS(depth, path):
    if len(path) == n:
        temp = [['.'] * n for _ in range(n)]
        for i in path:
            temp[i[0]][i[1]] = 'Q'
        res.append([''.join(t) for t in temp])
        # temp.append([''.join(r) for r in cur])
        return

    for i in range(depth, n):
        for j in range(n):
            if isValid(i, j, path):
                path.append([i, j])
                DFS(i + 1, path)
                path.pop()

DFS(0, [])
print(res)





