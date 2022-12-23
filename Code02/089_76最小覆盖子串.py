s = "ADOBECODEBANC"
t = "ABC"

import collections

need = collections.Counter(t)
needLen = len(t)
# print(type(need))
st = en = None
beg = 0
end = 0
res = ''

while end < len(s):
    # 滑入
    inch = s[end]
    if inch in t:
        if need[inch] > 0:
            # 是否有效地减小目标字符串
            needLen -= 1
        need[inch] -= 1

    # 判断是否已经满足
    while needLen == 0:
    # 如果满足则尝试缩小窗口; 滑出
        if en == None or beg - end + 1 < en - st + 1:
            st = beg
            en = end
        
        # 滑出
        outch = s[beg]
        if outch in t:
            need[outch] += 1
            if need[outch] > 0:
                needLen += 1
        beg += 1
    end += 1

if st == None:
    print("")
else:
    print(s[st:en+1])





