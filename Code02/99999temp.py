def func(s, result):
    if len(s) == 1:
        if int(s[0]) == result:
            return 1
        else:
            return 0

    res = 0
    for op in range(1, len(s), 2):
        # 确保每次都能压中运算符
        l0 = func(s[:op], 0)
        l1 = func(s[:op], 1)
        r0 = func(s[op + 1:], 0)
        r1 = func(s[op + 1:], 1)
        
        if s[op] == '&':
            if result == 1:
                res += l1 * r1
            else:
                res += l0 * r1 + l1 * r0 + l0 * r0
        elif s[op] == '|':
            if result == 1:
                res += l1 * r1 + l0 * r1 * l1 * r0
            else:
                res += l0 * r0
        else:
            # s[op] == '^'
            if result == 1:
                res += l0 * r1 * l1 * r0
            else:
                res += l0 * r0 + l1 * r1
    return res

s = "1^0|0"
result = 0
res = func(s, result)
print(res)  