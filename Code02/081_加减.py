
def add(a, b):
    if a & b == 0:
        return a ^ b
    t = a ^ b
    j = a & b
    return add(t, j << 1)

def add1(a, b):
    sum = a
    while b != 0:
        sum = a ^ b
        b = (a & b) << 1
        a = sum
    return sum

def minus(a, b):
    return add1(a, add1(~b, 1))

def minus2(a, b):
    while b != 0:
        temp = a ^ b
        b = ((a ^ b) & b) << 1
        a = temp

    return a 


import random
times = 100
for i in range(times):
    # a = random.randint(1, 1000)
    # b = random.randint(1, 1000)
    # if add1(a, b) != a + b:
    #     break

    # a = random.randint(1, 100)
    # b = random.randint(-1000, -1)
    # if minus(a, b) != (a - b):
    #     break

    a = random.randint(1111, 10000)
    b = random.randint(1, 100)
    if minus2(a, b) != (a - b):
        break





if i == times - 1:
    print("wuhu!")
else:
    print("Error!!!!")





