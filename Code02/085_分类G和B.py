s = 'BBBBBBGGBGGB'

hold1 = 0
hold2 = 0

count1 = 0
count2 = 0

for index in range(len(s)):
    if s[index] == 'G':
        count1 += index - hold1
        hold1 += 1
    if s[index] == 'B':
        count2 += index - hold2
        hold2 += 1

print(count1, count2) 
print(min(count1, count2)) 