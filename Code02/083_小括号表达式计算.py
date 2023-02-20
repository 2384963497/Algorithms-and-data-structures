grid = [[0,1],[1,0]]
# [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
from collections import deque

M = len(grid[0])
N = len(grid)
# 方向偏移
dir = ((0, 1), (0, -1), (1, 0), (-1, 0))

# 
def markIsland(x, y):
    markQue = deque()
    tempQue = deque()

    tempQue.append((x, y))
    while len(tempQue) != 0:
        curX, curY = tempQue.popleft()
        grid[curX][curY] = 2
        tempQue.append((curX, curY))

        for i, j in dir:
            tX = curX + i
            tY = curY + j
            if tX < 0 or tY < 0 or tX >= N or tY >= M or grid[tX][tY] != 1:
                continue
            markQue.append((tX, tY))
    return tempQue
        

    

# 扫描到第一座岛
f = False
for i in range(M):
    for j in range(N):
        if grid[i][j] == 1:
            tempQue = markIsland(i, j)
            f = True
            break
    if f:
        break


# 开始多源bfs，直到碰到第二座岛
step = 1
while True:
    nowLen = len(tempQue)
    for i in range(nowLen):
        curX, curY = tempQue.popleft()
        grid[curX][curY] = 2

        for i, j in dir:
            tX = curX + i
            tY = curY + j
            if not (tX < 0 or tY < 0 or tX >= N or tY >= M):
                if grid[tX][tY] == 1:
                    print(step - 1)
                    input("wait")
                elif  grid[tX][tY] == 0:
                    tempQue.append((tX, tY))

    step += 1