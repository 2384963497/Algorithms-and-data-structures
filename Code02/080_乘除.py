def add(a, b):
    temp = a ^ b
    b = (a & b) << 1
    while b != 0:
        t = temp ^ b
        b = (temp & b) << 1
        temp = t
    return temp
    
def times1(a, b):
    res = 0
    while b != 0:
        if b & 1 == 1:
            res = add(res, a)
        a <<= 1
        b >>= 1
            
    return res


        
        

import random
times = 10
for i in range(times):
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    if times1(a, b) != a * b:
        break





if i == times - 1:
    print("wuhu!")
else:
    print("Error!!!!")

