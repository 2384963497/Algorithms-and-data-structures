# Other

[toc]





---

## leetCode146 LRU 缓存

*   问题描述
    *   [问题地址](https://leetcode.cn/problems/lru-cache/description/)
*   解题思路
    *   双向链表 + 哈希表
    *   双向链表用于保存相对次序，双向链表在中间节点移除时时间复杂度是O(1)
    *   哈希表可以解决链表遍历O(n)复杂度的问题，可以降到O(1)
    *   插入一个节点
        *   判断该节点key是否已经存在；使用哈希表
            *   如果存在，那么就要更新原来的节点的相对位置，将它移动到链表的结尾
            *   如果不存在，那么追加到末尾，并登记在哈希表中
    *   查询一个节点
        *   判断是否存在该节点
            *   如果存在，返回对应值，并且要更新它的相对位置，将它移到末尾
            *   如果不存在，返回指定值

*   实现代码

    *   ```python
        class Node():
            def __init__(self, key, val):
                self.key = key
                self.val = val
                self.last = None
                self.next = None
        
        class doubleLink():
            def __init__(self):
                self.head = None
                self.tail = None
            
            def append(self, node):
                if self.head == None:
                    # 当前为空链表
                    self.head = node
                    self.tail = node
                else:
                    self.tail.next = node
                    node.last = self.tail
                    self.tail = node
        
            def remove(self, node):
                if self.head == self.tail:
                    # 删除唯一节点
                    self.head = None
                    self.next = None
                elif node.last == None:
                    # 删除头节点
                    self.head = node.next
                    node.next.last = None
                elif node.next == None:
                    # 删除尾节点
                    self.tail = node.last
                    node.last.next = None
                else:
                    # 普遍节点
                    node.next.last = node.last
                    node.last.next = node.next
        
        class LRUCache:
            def __init__(self, capacity: int):
                self.MAX = capacity
                self.len = 0
                self.Map = dict()
                self.link = doubleLink()
        
            def get(self, key: int) -> int:
                res = self.Map.get(key)
                if res == None:
                    return -1
                # 访问有效值要更新相对位置
                self.link.remove(res)
                # 移除后重新插入所以需要将节点重置，不能有之前的位置信息，这样才能正确追加到链表末尾
                res.last = None
                res.next = None
                self.link.append(res)
                return res.val
        
            def put(self, key: int, value: int) -> None:
                tempNode = Node(key, value)
                if self.Map.get(key) != None:
                    # key已经存在
                    self.link.remove(self.Map[key])
                    self.Map.pop(key)
                    self.len -= 1
                # 追加
                self.link.append(tempNode)
                self.Map[key] = tempNode
                self.len += 1
                if self.len > self.MAX:
                    # 长度超出
                    self.Map.pop(self.link.head.key)
                    self.link.remove(self.link.head)
                    self.len -= 1
        ```









---

## leetCode55 跳跃游戏

*   问题描述

    *   [问题地址](https://leetcode.cn/submissions/detail/392417914/)

*   解题思路

    1.   可以使用动规思路解；但是时间复杂度是O(n^2) 空间复杂度是O(n)

    2.   
         *   维护一个当前步数能到达的最大范围curMax，并维护一个下一个步数能到达地的最大范围nextMax
         *   从当前范围到下一层范围的条件就是步数+1(如果题目需要统计步数)
         *   如果当前指针在当前的最大窗口内那么可以尝试用当前位置的值更新nextMax
         *   前提是如果通过当前值再跳一步的范围大于nextMax
         *   如果当前指针不在当前最大的窗口范围内，那么就跨一步，并且进入下一层范围；
         *   再次判断当前范围内的值能否拓宽nextMax；遇到0则要判断nextMax是否最大只能达到当前0位置；
         *   如果是，则证明无法跳跃到终点(如果是最后一个位置的0则能到达终点)，不是则继续执行尝试更新nextMax和移动当前指针的操作

*   实现代码

    *   ```python
        class Solution:
            def canJump(self, nums: List[int]) -> bool:
                if len(nums) == 1:
                    return True
                # step = 0
                curMax = 0
                nextMax = None
        
                for i in range(len(nums) - 1):
                    # 这里不需要走到最后一个位置；因为倒数第二个位置如果合法那么就一定能抵达最后，所以只需要判断到倒数第二即可;
                    if curMax < i:
                        # step += 1
                        # 因为从当前最大范围进入下一层最大范围的条件就是步数+1
                        curMax = nextMax
                    nextMax = nums[i] + i if nextMax == None or nextMax < nums[i] + i else nextMax
                    if nums[i] == 0 and nextMax == i:
                        return False
                return True
        ```



---

## leetCode149 直线上最多的点数:star:

*   问题描述

    *   [问题地址](https://leetcode.cn/problems/max-points-on-a-line/description/)

*   解题思路

    *   只能穷举没过每一个点的每一条直线
    *   统计过每一个点每一种斜率的点个数，再求过当前点覆盖点最多的个数，最后返回所有点中最大的
    *   斜率为正无穷时需要单独统计`l:30`，还需要考虑重合点的情况`l:29`；
    *   细节
        -   线上的点其实时组合关系，如果在处理a点时处理过ab这条线，那么就没有必要处理ba这条线
        -   在求斜率存入字典时，需要注意，因为程序中除法存在精度丢失的情况，**如果直接(y1-y2)/(x1-x2)然后作为斜率统计那么可能出现两个斜率并不相同的点被统计到一个斜率上**1,00000000000000001就会和斜率为1的点被统计到一条直线上；为了避免应该选择用分数的形式约分后统计
        -   约分就涉及到求最大公约数，可以用辗转相除求
        -   **在字典中找出最大的val值**`l:45`

*   实现代码

    *   ```python
        class Solution:
            def maxPoints(self, points: List[List[int]]) -> int:
                resList = []
                
                def func(x, y):
                    # 求两个数的最大公约数
                    if x == 0:
                        return '0'
                    if abs(x) < abs(y):
                        a = abs(x)
                        b = abs(y)
                    else:
                        a = abs(y)
                        b = abs(x)
                    
                    # 辗转相除
                    res = b % a
                    while res != 0:
                        b = a
                        a = res
                        res = b % a
        
                    # 同号
                    if x > 0 and y > 0 or x < 0 and y < 0:
                        return str(abs(x) // a) +'_' + str(abs(y) // a)
                   	# 异号
                    else:
                        return '-' + str(abs(x) // a) +'_' + str(abs(y) // a)
                    # 以'a_b'的形式返回作为字典的key
        
                for i in range(len(points)):
                    same = 0
                    sameX = 0
                    other = dict()
                    for j in range(i, len(points)):
                        if points[j][0] == points[i][0] and points[j][1] == points[i][1]:
                            # 同一点
                            same += 1
                        elif points[j][0] == points[i][0]:
                            sameX += 1
                        else:
                            temp = func(points[i][1] - points[j][1], points[i][0] - points[j][0])
                            other[temp] = other.get(temp, 0) + 1
                    if len(other) != 0:
                        res = other[max(other, key = lambda x : other[x])]
                    else:
                        res = 0
                    res = max(res, sameX) + same
                    resList.append(res)
                return max(resList)
                # return resList
        ```





---

## leetCode剑指 Offer 49. 丑数

*   问题描述
    *   [问题地址](https://leetcode.cn/problems/chou-shu-lcof/)	

-   解题思路

    -   因为最小的丑数规定为1，且往后的丑数都是较小的丑数成2、3、5得到的；所以可以从1推到第n个丑数
    -   定义三个指针，分别代表下一个丑数×2 下一个整数×3 下一个数×5
    -   每一轮都选择当前三个指针中最小的值(可能出现多个指针所指的值相同)，将最小的那个数的指针移动到下一个丑数上

-   实现代码

    -   ```python
        class Solution:
            def nthUglyNumber(self, n: int) -> int:
                res = [1]
                n -= 1
        
                p2 = 0
                p3 = 0
                p5 = 0
        
                for i in range(n):
                    temp = min(res[p2] * 2, res[p3] * 3, res[p5] * 5)
                    if res[p2] * 2 == temp:
                        p2 += 1
                    if res[p3] * 3 == temp:
                        p3 += 1
                    if res[p5] * 5 == temp:
                        p5 += 1
                    res.append(temp)
                
                return res[-1]
        ```

---

## 最小不可组成和

-   问题描述

    -   给定一个**正整数**数组arr，该数组所有子数组的和最小记作left，最大记作right，则在区间[left, right]上第一个正整数数组无法组成的数即为最小不可组成和，如果都能组合出，那么最小不可组成和就是right+1，将其返回

-   解题思路

    -   因为所有的数组元素都为正整数，所以最小子集和就是数组最小值min(arr), 最大子集和就是sum(arr)
    -   如此以来，问题就可以抽象成一个01背包问题；分别推算出在所有元素中能否组成[0, right]；最后遍历`DP[-1][left ~ right]`第一个出现False的下标值就是最小不可组成和；如果遍历结束都没遇到False则返回right+1

-   实现代码

    -   ```python
        # arr = [1, 2, 4]
        arr = [1, 11, 3]
        def DPfunc():
            left = min(arr)
            right = sum(arr)
        
            DP = [[False for j in range(right + 1)] for i in range(len(arr))]
            DP[0][0] = DP[0][arr[0]] = True
        
            for i in range(1, len(arr)):
                DP[i][0] = True
                for j in range(1, right + 1):
                    DP[i][j] = DP[i - 1][j] or (DP[i - 1][j - arr[i]] if j - arr[i] >= 0 else False)
            for j in range(left + 1, right + 1):
                if DP[-1][j] == False:
                    return j
            
            return right + 1
        ```

-   进阶问题

    -   如果现在能肯定数组中有1这个元素，请问能否实现比DP更快的算法输出最小不可组成和

-   解题思路

    -   先将数组升序排序
    -   定义一个范围area`l:3`, 初值赋为1；数组指针从1开始，范围变量表示当前指针之前的元素能拼出[1, area]
    -   如果当前指针所指元素 <= area`l:6`;说明当前所指元素在[1, area]，且当前位置之前能凑出[1, area]所有元素，那么加上当前元素area就能连续凑出[1, area + arr[i]] 更新area；如果一个当前值 > area + 1 [area, arr[i] - 1] 之前的数拼凑不出来，返回area+1
    -   例如如果当前值为9 而area为8  ； 9 <= area + 1 如果9加入，单独选9不需要area帮助能**将area这个连续的范围**扩充到9，如果选9让area帮忙解决1即可扩充到10；(因为area连续而且当前值合法的前提下是area中或者在area上届+1的位置)那么area在和当前值配合的情况下可以将范围扩充到[area+1, area+arr[i]]；如果当前值>area  + 1 证明area + 1 到当前值都之间的值都不可组成，返回area+1(因为当前位置及其往后的数都一定> area + 1，固然不可能再平凑出area + 1)
    -   "为什么要求数组中一定要有1?" 因为要保证area从一开始就是连续的，假设arr中最小的是3那么area就无法[1, 2]在这个区间上拼凑出来，排序也是必须的一步

-   实现代码

    -   ```python
        def rangeFunc(arr):
            arr.sort()
            area = 1
        
            for i in arr[1:]:
                if i <= area + 1:
                    # 合法
                    area += i
                else:
                    return area + 1
            return area + 1 
        ```









---

## leetCode08.14. 布尔运算

*   问题描述

    *   [问题地址](https://leetcode.cn/problems/boolean-evaluation-lcci/)

*   解题思路

    *   如果按每个运算符为最后结合分类；那么将可以不重不漏地统计所有有效方法；按该运算符分成左右两个部分再进行递归即可；
    *   递归的base case及是传入的表达式只有'0'或'1'两个字符时，此时如果字符为所需要的表达式值则返回1表示为一种有效方法；反之为0
    *   递归时要根据当前运算符选择下层递归时左右两边的所有合法情况和所需表达式值
    *   当得到两边所有合法方式数时将他们相乘，即可得到当前位置最后结合的所有不同合法情况
    *   如此这般，依次统计每个运算符 最后结合的情况
    *   优化：记忆化搜索

*   实现代码

    *   ```python
        class Solution:
            def countEval(self, s: str, result: int) -> int:
                res = 0
                memo = dict()
        
                def func(s, r):
                    # 记忆化搜索
                    if memo.get(s + str(r)) != None:
                        return memo[s + str(r)]
                    if len(s) == 1:
                        if int(s) == r:
                            return 1
                        else:
                            return 0
                    
                    count = 0
                    for i in range(1, len(s), 2):
                        # 每一次都一定指向逻辑运算符
                        cur = s[i]
                        # punchline
                        l0 = func(s[:i], 0)
                        l1 = func(s[:i], 1)
                        r0 = func(s[i + 1:], 0)
                        r1 = func(s[i + 1:], 1)
                        if cur == '|':
                            # 在分类时必须分清每一种运算符每一种运算结果的可能性；左右两边各有True和False两种情况；所以为4种不同情况
                            if r == 1:
                                count += l1 * r0 + l0 * r1 + l1 * r1
                            else:
                                count += l0 * r0
                        elif cur == '&':
                            if r == 1:
                                count += l1 * r1
                            else:
                                count += l1 * r0 + l0 * r0 + l0 * r1
                        else:
                            # ^ 不同为1 相同为0
                            if r == 1:
                                count += l1 * r0 + l0 * r1
                            else:
                                count += l1 * r1 + l0 * r0
        
                    # 记忆化搜索
                    memo[s + str(r)] = count
                    return memo[s + str(r)]
                
                res = func(s, result)
        
                return res
        ```







---

## leetCode517 超级洗衣机

*   问题描述
    *   [问题地址](https://leetcode.cn/problems/super-washing-machines/description/)

*   解题思路

    *   总体思路和最长自增子序列类题大体相同——求出每个位置的瓶颈或最优解，最终在综合每个位置求出最终解
    *   此题中，如果计算得到每个位置需要运行的轮次，那么最终的答案就是所有位置中的最大值
    *   如果最终能平分，那么每个位置上的最终值都是一样的，且可以轻松计算得到`l:12`
    *   一个位置的左侧和，右侧和也可以轻松得到；如果当前位置的左右两侧所需都为负数，证明当前位置要分别像左右两侧运送衣服；
    *   那么当前位置的值就是两边所需件数和的绝对值`l:21`；因为要向两侧运送衣服只能一件一件地运，运送一个位置一轮中只能向一个方向送衣服
    *   否则，当前位置的运行轮次就是两侧值的绝对值中的较大者`l:23`

*   实现代码

    *   ```python
        class Solution:
            def findMinMoves(self, machines: List[int]) -> int:
                LEN = len(machines)
                SUM = sum(machines)
                if LEN == 1:
                    return 0
                if SUM % LEN != 0:
                    # 不可能被平分
                    return -1
                
        
                target =  SUM // LEN
                
                res = -1
                lSum = 0
        
                for i in range(LEN):
                    lNeed = lSum - i * target
                    rNeed = (SUM - lSum - machines[i]) - (target * (LEN - i - 1))
                    if lNeed < 0 and rNeed < 0:
                        temp = abs(lNeed + rNeed)
                    else:
                        temp = max(abs(lNeed), abs(rNeed))
                    lSum += machines[i]
                    res = max(res, temp)
                
                return res
        ```



---

## step sum

*   问题描述

    *   step sum定义：一个数的步骤和 为该数字依次抹去最右侧数字的数值之和
    *   例如 132： 132 + 13 + 1 = 146 那么146就是132的步骤和
    *   给定一个数字n，如果是某个数字m的步骤和则返回m，如果不是则返回 -1

*   解题思路

    *   单调性 就要 联想到二分
    *   如果A > B，A的步骤和为a，B的步骤和为b那么 一定有a > b
    *   所以该题可以用二分

*   实现代码

    *   ```python
        num = 269
        
        left = 0
        right = num
        
        def getStepSum(n):
            res = 0
            while n:
                res += n
                n //= 10
            return res
        
        while left <= right:
            mid = (left + right) // 2
            temp = getStepSum(mid)
            if temp == num:
                break
            elif temp < num:
                left = mid + 1
            else:
                right = mid - 1
        
        if left > right:
            print(-1)
        else:
            print(mid)
        ```

















---

## leetCode

*   问题描述
    *   [问题地址]()

