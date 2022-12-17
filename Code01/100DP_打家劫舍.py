nums = [2,7,9,3,1]

a = nums[0]
b = nums[1] if nums[1] > nums[0] else nums[0]


for i in range(2, len(nums)):
    if a + nums[i] > b:
        c = a + nums[i] 
    else:
        c = b
    a = b
    b = c

# return DP[-1]
print(c)



