nums = [1,2,3]

a = nums[0]
b = max(nums[0], nums[1])
c = b
for i in range(2, len(nums) - 1):
    if a + nums[i] > b:
        c = a + nums[i] 
    else:
        c = b
    a = b
    b = c
r1 = c

a = nums[1]
b = max(nums[1], nums[2])
c = b
for i in range(3, len(nums)):
    if a + nums[i] > b:
        c = a + nums[i] 
    else:
        c = b
    a = b
    b = c
r2 = c

print(max(r1, r2))
# return DP[-1]
# print(c)



