nums = [10,9,2,5,3,7,101,18]

DP = [1 for i in nums]

for i in range(1,len(nums) + 1):
    if nums[i] > nums[i - 1]:
        DP[i] = DP[i - 1] + 1
    else:
        DP[i] = DP[i - 1]

print(DP[-1])