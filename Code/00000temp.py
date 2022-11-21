


begin = int(input())
end = int(input())

count = 0
while begin <= end:
    t = begin 
    while t:
        if t % 10 == 2:
            count += 1
        t /= 2
    begin += 1
print(count)
















