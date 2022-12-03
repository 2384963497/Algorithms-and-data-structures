text1 = "abc"
text2 = "def" 

# 递归函数返回 字符串1 [0:x+1] 位置上 和 字符串2 [0:y+1] 上的最长公共子序列
def func(x, y):
    if x == 0 and y == 0:
        return 1 if text2[0] == text1[0] else 0
    elif x == 0:
        if text1[0] in text2[0:y + 1]:
            return 1
        else:
            return func(x, y - 1)
    elif y == 0:
        if text2[0] in text1[0:x + 1]:
            return 1
        else:
            return func(x - 1, y)
        
    else:# 分成三种模型
        r1 = 0
        if text1[x] == text2[y]: # 两字符串最后一个字符串相同
            r1 = func(x - 1, y - 1) + 1
        r2 = func(x - 1, y)
        r3 = func(x, y - 1) 
        return max(r1, r2, r3)

print(func(len(text1) - 1, len(text2) - 1))






