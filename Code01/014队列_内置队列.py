# rt
# import queue
from collections import deque   #双端队列
dequeQueue = deque(['Eric','John','Smith'])
print(dequeQueue.__len__())
dequeQueue.append('Tom')    #在右侧插入新元素
dequeQueue.appendleft('Terry')  #在左侧插入新元素
print(dequeQueue)
dequeQueue.rotate(2)    #循环右移2次
print('循环右移2次后的队列',dequeQueue)
dequeQueue.popleft()    #返回并删除队列最左端元素
print('删除最左端元素后的队列：',dequeQueue)
dequeQueue.pop()    #返回并删除队列最右端元素
print('删除最右端元素后的队列：',dequeQueue)
