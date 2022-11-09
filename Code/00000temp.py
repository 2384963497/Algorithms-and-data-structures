from collections import deque
t = deque([1,2,3,4,5,6,7,8])
# print(t.__len__())
print(t.popleft())

t.append('w')
print(t.pop())