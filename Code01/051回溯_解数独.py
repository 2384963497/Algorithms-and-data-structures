
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

def isValid(x, y):
    for i in range(9):
        # 判断行的有效性
        if board[x][i] == board[x][y] and i != y:
            return False
        # 判断列的有效性
        if board[i][y] == board[x][y] and i != x:
            return False
    # 判断所处九宫格
    i = x - x % 3
    t1 = i + 3
    j = y - y % 3
    t2 = j + 3

    while i < t1:
        j = t2 - 3
        while j < t2:
            if board[i][j] == board[x][y] and i != x and j != y:
                return False
            j += 1
        i += 1
    return True

flag = True
def func(x, y):
    global flag

    def DFS(x, y):
        global flag
        for i in range(1, 10):
            if flag:
                board[x][y] = chr(48 + i)
                if isValid(x, y):
                    # 找到下一个空白格，进入下一次递归
                    x1 = x
                    y1 = y
                    while board[x1][y1] != '.':
                        y1 += 1
                        x1 += y1 // 9
                        y1 %= 9
                        if x1 == 9:
                            flag = False
                            return
                    DFS(x1, y1)
                if i == 9 and flag:
                    board[x][y] = '.'
                    return


    while board[x][y] != '.':
        y += 1
        x += y // 9
        y %= 9
        if x == 9:
            flag = False
            return
    DFS(x, y)

func(0, 0)
# return board
for i in board:
    print(i)






















