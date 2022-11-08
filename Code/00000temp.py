def sReversed(s):
    if len(s) == 1:
        return s
    else:
        return s[-1]+sReversed(s[0:-1])

s = input("请输入需要逆置的字符串")
r = sReversed(s)
print(r)


