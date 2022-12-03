

# def tryFunc(i, j, flag):
#     if i + 1 == j:
#         if s[i] == s[j]:
#             return 1 if flag == 1 else 2 
#         else:
#             return 1
#     elif i == j:
#         return 1
#     if i > j:
#         return 1

#     if s[i] == s[j]:
#         return tryFunc(i + 1, j - 1, 2) + (1 if flag == 1 else 2) 
#     r1 = tryFunc(i + 1, j, 2 if flag == 2 else 1)    
#     r2 = tryFunc(i, j - 1, 2 if flag == 2 else 1)
#     return max(r1, r2)    


# print(tryFunc(0, len(s) - 1, 2))
s = "abcdef"
# s = 'aba'

def tryFunc(i, j):
    if i == j:
        return 1
    elif i + 1 == j:
        if s[i] == s[j]:
            return 2
        else:
            return 1
    
    
    r0 = 0
    if s[i] == s[j]:
        r0 = tryFunc(i + 1, j - 1) + 2
    r3 = tryFunc(i + 1, j - 1)
    r1 = tryFunc(i + 1, j)
    r2 = tryFunc(i, j - 1)
    return max(r1, r2, r0, r3)
    


print(tryFunc(0, len(s) - 1))






