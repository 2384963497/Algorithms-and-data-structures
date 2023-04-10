# 	13思路&技巧笔记(Python)



---

## Python内置堆、栈、队列及其使用

*   [相关文章](https://blog.csdn.net/jamfiy/article/details/88188595)

    *   ```python
        from collections import deque   #双端队列
        dequeQueue = deque(['Eric','John','Smith'][,n]) #可以指定队列的固定长度; 队满时自动出队再入队
        print(dequeQueue)
        
        dequeQueue.append('Tom')    #在右侧插入新元素
        dequeQueue.appendleft('Terry')  #在左侧插入新元素
        print(dequeQueue)
        dequeQueue.popleft()    #返回并删除队列最左端元素
        print('删除最左端元素后的队列：',dequeQueue)
        dequeQueue.pop()    #返回并删除队列最右端元素
        print('删除最右端元素后的队列：',dequeQueue)
        ```







---

-   ```python
    import collections
    a = '12321314'
    a = [4, 324, 576, 5]
    temp = collections.Counter(a)
    ```

    -   collections中的Counter函数能将对象统计后返回词频字典

-   ```python
    s = 'absdsagervd'
    res = sorted(s, key = lambda x:ord(x))
    ```

    -   内置函数指定较简单的比较器	

-   自定义比较器:star:

    -   ```python
        mport random
        from functools import cmp_to_key
        
        classes = [(random.randint(100,200), random.randint(1,100)) for i in range(20)]
        
        def cmp(val1, val2):
            if val1[0] > val2[0]:
                return -1
            elif val1[0] < val2[0]:
                return 1
            else:
                if val1[1] > val2[1]:
                    return 1
                elif val1[1] < val2[1]:
                    return -1
                return 0
        print(classes, end = '   \n\n')
        classes.sort(key = cmp_to_key(cmp))
        print(classes)
        ```

    -   `from functools import cmp_to_key`

    -   比较器中-1表示要较小值，或者需要排前面的值

-   python内置进制转换

    -   `int(C, <目标进制>)`
    -   可以用指定进制抓换n，是字符
    -   如果要用数值转进制则要使用函数`bin(), otc(), hex()`
    -   python数值进制表示前缀`0b1011, 0o1571, 0x1a12b`

-   ```python
    path = path.lstrip('/') # 删除指定前导字符
    ```



---



-   `help('内容')`可以显示内容的一些相关信息，如果忘记了某些知识点或者操作可以使用它

-   ```python
    dic = {'1':123, '2':321}
    for k, v in dic.items():
        print(k, end = ' ')
        print(v)
    
    # 1 123
    #2 321
    ```

-   跳出多层循环：可以将遍历循环写到函数中，需要跳出时直接在内层return

-   ```python
    深度拷贝
    from copy import *
    old = [[1, 2, 3, 4], '11', 4]
    new0 = old
    new1 = old[:]
    new2 = old.copy()
    new3 = copy(old)
    new4 = deepcopy(old)
    
    old[-1] = 'change1'
    old[0][1] = 'Flag'
    print("new0", new0)
    print("new1", new1)
    print("new2", new2)
    print("new3", new3)
    print("new4", new4)
    
    # new0 [[1, 'Flag', 3, 4], '11', 'change1']
    # new1 [[1, 'Flag', 3, 4], '11', 4]
    # new2 [[1, 'Flag', 3, 4], '11', 4]
    # new3 [[1, 'Flag', 3, 4], '11', 4]
    # new4 [[1, 2, 3, 4], '11', 4]
    ```

-   ```python
    # 正负无穷
    maxNum = float('INF')
    minNum = -float('inf') # 或float('-inf')
    ```

-   :star:

    ```python
    # 默认字典
    
    dict1 = dict()
    
    dict1['p1'].add('new')
    dict1['p1'] = {123, 211}
    print(dict1)
    # 以上代码会报错
    
    from collections import defaultdict
    # 参数表示如果当前key不出在，自动视作什么类型
    from collections import defaultdict
    dict1 = defaultdict(set)
    
    dict1['p1'].add('new')
    print(dict1['p1'])
    dict1['p1'] |= {123, 211}
    print(dict1['p1'])
    
    #####
    from collections import defaultdict
    dict1 = defaultdict(int)
    
    print(dict1[3])
    # 
    ```

-   :star:可以用字典高效地表示图；

    -   ```python
        graph = {
            1:{2, 3}
            2:{1, 3}
            3:{1, 2}
        }
        graph = {
            1:{(2, 5), (3, 10)
        }
        ```


*   :star:排列与组合

    *   ```python
        from itertools import combinations, permutations
        return list(permutations(nums))
        return list(combinations([i for i in range(1, n + 1)], k))
        ```

    *   组合必须指定长度，排列可以不指定长度

*   ```python
    any(o)	# 可迭代对象中只要有一个True就返回True
    all(o)	# 可迭代对象中全为True才返回True
    
    nums1 = [1, 3, 5, 7]
    nums2 = [1, 3, 5, 6, 9]
    print(any([nums1[i] < 10 for i in range(len(nums1))]))	# True
    print(all([nums1[i] & 1 == 0 for i in range(len(nums1))]))	# False
    ```

*   ```python
    from decimal import *
    import decimal
    print(2 / 7)
    print(Decimal(2) / Decimal(7))
    decimal.getcontext().prec = 100
    print(Decimal(2) / Decimal(7))
    ```

    *   python高进度数学运算

-   :star:map

    -   ```python
        # map
        map(pow, [1, 2, 3, 4])
        
        # 接收输入的两个整数15  23
        temp = map(int, input().split())
        
        
        h = int(input())  # 输入数据
        W = [list(map(int, input().split())) for i in range(h)]
        ```
        
    -   map返回的是一个迭代器对象

    -   将对象通过指定方法进行映射

-   :star:前缀和 

    -   ```python
        from itertools import *
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        res = list(accumulate(nums))
        print(res)
        # [1, 3, 6, 10, 15, 21, 28, 36]
        ```

*   :star:.format()函数

    *   ```python
        # 3.1415926	{:.2f}	3.14	保留小数点后两位(四舍五入)
        # 3.1415926	{:+.2f}	+3.14	带符号保留小数点后两位
        # 2.71828	{:.0f}	3	不带小数
        # 5	{:0>2d}	05	数字补零 (填充左边, 宽度为2)  < 左对齐  >右对齐 ^ 居中对齐， 对齐方式的左边字符表示的是空白处填充字符
        # 0.25	{:.2%}	25.00%	百分比格式（四舍五入）
        # 1000000000	{:.2e}	1.00e+09	指数记法  指定的是e前面的长度 E可以大写
        {:d}{:o}{:x}{:#x}{:b} 不同进制表示方式 十六进制带#则会加上0x前缀
        ```

*   :star:日期时间库

    *   [相关文章](https://blog.csdn.net/cmzsteven/article/details/64906245)

    *   ```python
        import datetime
        today = datetime.date.today()
        
        today = datetime.date(2002, 3, 15)
        print(today.day)
        print(today.month)
        print(today.year)
        print(today, type(today))
        print(today.weekday()) # 0是代表星期一
        
        
        #####
        # 两个日期比较大小 a > b
        a.__bt__(b)
        # 两个日期比较大小 a >= b
        a.__be__(b)
        # 两个日期比较大小 a < b
        a.__lt__(b)
        # 两个日期比较大小 a == b
        a.__eq__(b)
        # 两个日期比较大小 a != b
        a.__ne__(b)
        
        # 两个日期相差天数 x - y
        x.__sub__(y)	# 返回值是date.timedelta类
        
        # 更新日期
        Day = Day.replace(year = 2022)	# 注意！要更新！
        
        import datetime
        today = datetime.date.today()
        print(today)
        
        today = today + datetime.timedelta(days = -1)	# 日期加减
        
        print(today)
        
        Day = datetime.datetime.strptime('02/03/21', '%d/%m/%y')
        # 将输入字符串按格式串转换为时间型；只有日期无时间则默认0:0:0
        print(datetime.datetime.strftime(Day, '%y/%m/%d'))
        # 将时间型按格式串转换为字符串
        
        ```

*   设置递归的最大深度

    *   ```python
        import sys
        sys.setrecursionlimit(100000)
        ```

*   异常处理

    *   ```python
        try:
        	操作
        except Exception as e:
        	# 错误执行
        else:
        	# 正常执行
        ```

-   int不会四舍五入；需要使用format





---

-   快速幂
-   时间处理函数
-   math库
-   数据输入
-   差分
-   并查集





-   二维前缀和

    -   ```python
        # 维护
        pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + m[i][j]
        # 查询 x1,y1 x2,y2矩阵的前缀和; 注意边界判断
        res = pre[x2][y2] - pre[x1 - 1][y2] - pre[x2][y1 - 1] + pre[x1 - 1][y1 - 1]
        
        ```

-   差分

    -   ```python
        # 维护
        d[i] = nums[i - 1] - nums[i]
        
        # 区间更新 [l, r] + n
        d[l] += n
        d[r + 1] -= n
        	
        # 查询nums[q]
        pre = nums[0]
        i = 1
        while i != q:
            pre = pre += d[i]
            i += 1
        return pre
        ```

    -   差分区间查询的时间浮渣度已然是O(n)

-   唯一分解定理

    -   ```
        ```

    -   
