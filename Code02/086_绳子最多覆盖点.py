arr = [1, 3, 8, 9, 13, 14, 17, 20, 26, 88]
K = 10

def func1(arr, K):
    maxLen = -1
    left = 0
    now = 0 # 当期窗口内的合法点
    res = -1
    for right in range(len(arr)):
        # 窗口向右扩大一个点
        now += 1

        while arr[right] - arr[left] > K:
            # 需要收缩当前窗口
            left += 1
            now -= 1
        # 经过上面的循环后的窗口必定合法
        if maxLen < now:
            maxLen = now
            res = left
    print(maxLen, res)


def func2(arr, K):
    res = -1
    maxLen = -1
    now = 0

    left = 0
    for right in range(len(arr)):
        # 右侧窗口扩大
        now += 1
        # 收缩到合法窗口大小
        while arr[right] - arr[left] > K:
            left += 1
            now -= 1
        if now > maxLen:
            maxLen = now
            res = left
    print(maxLen, res)

func1(arr, K)
func2(arr, K)