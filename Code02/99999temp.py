import collections
s = 'ab'
t = 'b'
need = collections.Counter(t)
needLen = len(t)

start = end = None
left = right = 0
while right < len(s):
    # 滑入窗口
    temp = s[right]
    if temp in t:
        need[temp] -= 1
        if need[temp] >= 0:
            needLen -= 1

    # 判断是否能收缩当前有效解窗口
    while needLen == 0:
        if start == None or end - start > right - left:
            start = left
            end = right
        # 滑出
        temp = s[left]
        if temp in t:
            need[temp] += 1
            if need[temp] > 0:
                needLen += 1
        left += 1
    right += 1

print(s[start:right + 1])