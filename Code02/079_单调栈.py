heights = [2,1,5,6,2,3]
info = [None] * len(heights)
# 先利用单调栈求出每个位置最左和最右第一个小于当前值的位置
stack = []
for i in range(len(heights)):
    while stack != [] and heights[i] < heights[stack[-1]]:
        info[stack[-1]] = (-1 if len(stack) == 1 else stack[-2], i)
        stack.pop()
            
    stack.append(i)

i = len(stack) - 1
while i > 0:
    info[stack[i]] = (stack[i - 1], -1)
    i -= 1
info[stack[0]] = (-1, -1)
print(info)