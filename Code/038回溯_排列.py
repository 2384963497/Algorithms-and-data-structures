# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。


def backtracking(startNum, nowList):
    if len(nowList) == k:
        res.append(nowList[:])
        return
    
    for i in range(startNum, n+1):
        if n - i + len(nowList) + 1 < k:
            break
        nowList.append(i)
        backtracking(i + 1, nowList)
        nowList.pop()



if __name__ == '__main__':
    n = int(input(""))
    k = int(input(""))
    res = []    
    backtracking(1, list())
    print(res)

