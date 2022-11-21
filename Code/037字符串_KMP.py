def getNext(s):
    if len(s) <= 1: # 一个字符
        return [-1]
    next = [None for i in range(len(s))]   # 创建同长度的next列表
    next[0] = -1
    next[1] = 0
    for i in range(2, len(s)):
        t = next[i - 1]
        while t != -1:
            if s[t] == s[i - 1]:    # 尝试不同的位置与i-1比较
                next[i] = t + 1
                break
            else:
                t = next[t]
        if t == -1:
            next[i] = 0
    return next

def KMP(s1, s2):
    next = getNext(s2)

    i = 0   # s1的下标
    j = 0   # s2的下标
    while i < len(s1):
        if s1[i] == s2[j]:
            i += 1
            j += 1
            if j == len(s2):
                return i - j
        else:
            j = next[j]
        if j == -1:
            j = 0
            i += 1
    return None



if __name__ == '__main__':
    s1 = "asd26asdasdba-565"
    s2 = "asdba"

    pos = KMP(s1, s2)
    if pos == None:
        print("s1 doesn't contain s2")
    else:
        print(pos)