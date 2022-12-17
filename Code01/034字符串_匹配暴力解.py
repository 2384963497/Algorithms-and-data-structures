
s1 = "123456"
s2 = "456"

Flag = False
for i in range(len(s1)):
    if s1[i] == s2[0]:
        x = i
        y = 0
        while y < len(s2) and s1[x] == s2[y]:
            x += 1
            y += 1
        if y == len(s2):
            Flag = True
            break

print(Flag)


