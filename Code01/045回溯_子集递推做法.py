
nums = [1, 2, 3]
res = [[]]
for i in nums:
    res = res + [x + [i] for x in res]    
print(res)



