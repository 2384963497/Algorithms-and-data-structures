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



