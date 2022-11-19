# n皇后问题
# 要在n*n的矩阵中放下n个皇后，要求每个皇后之间都不能共列、不能共行、不能共斜线
# 输入一个n 输出在这个n阶矩阵中有多少种合法的放法
# n=8 输出 92

def isValid(x, y):
    for i in range(n):
        if Map[i][y] == 1:
            return False
    for i in range(n):
        for j in range(n):
            if Map[i][j] == 1 and abs(x-i) == abs(y-j):
                return False
    return True
def dfs(x):
    global count
    if x == n:
        count += 1
        return 
    for y in range(n):
        if isValid(x, y):
            Map[x][y] = 1
            dfs(x+1)
            Map[x][y] = 0
    
if __name__ == '__main__':
    n = int(input("n = "))
    count = 0
    Map = [[None for i in range(n)] for j in range(n)]
    dfs(0)
    print(f"{n}阶矩阵有{count}种摆法")