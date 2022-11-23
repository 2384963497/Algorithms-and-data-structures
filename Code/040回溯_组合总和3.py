# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
# 只使用数字1到9
# 每个数字 最多使用一次 
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。


if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    candidates.sort()
    res = []

    def backTracking(stratIndex, nowList):
        if sum(nowList) == target:
            res.append(nowList[:])
            return
        
        for i in range(stratIndex, len(candidates)):
            if i>0 and candidates[i] == candidates[i-1]:
                i += 1
                continue
            nowList.append(candidates[i])
            backTracking(i + 1, nowList)
            nowList.pop()
    backTracking(0, [])
    # return res
    print(res)


