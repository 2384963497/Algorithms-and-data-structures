nums = [3,2,1,0,4]
DP = [-1] * len(nums)
DP[-1] = 0
for i in range(len(nums) - 2, -1, -1):
    temp = -1
    for j in range(nums[i] + 1):
        if i + j > len(nums) - 1:
            break
        else:
            temp = max(temp, DP[i + j])
    DP[i] = temp

if DP[0] == -1:
    print(False)
print(True)