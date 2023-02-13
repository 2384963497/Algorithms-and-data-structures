# str = "48*((70-65)-43)+8*1"
# str = "-14*(-1)*2+(-8*2*(2+3))-20"
str = "-81+1"

def func(s, begin):
    stack = []
    
    i = begin

    nums = 0
    while i < len(s):
        if s[i] >= '0' and s[i] <= '9':
            nums = nums * 10 + int(s[i]) 
        elif s[i] == '(':
            nums, i = func(s, i + 1)
        elif s[i] == ')':
            break
        else:
            # 当前字符必定为运算符
            if stack != [] and stack[-1] in '*/':
                # 栈顶需要提前运算的乘除情况
                x = stack.pop()
                a = stack.pop()
                stack.append(a * nums if x == '*' else a / nums)
            else:
                # +-情况；或者是空栈的情况，此时同样压入nums再压入*/运算符
                stack.append(nums)
            nums = 0
            stack.append(s[i])
        
        i += 1

    # 再出push当前的nums
    if stack != [] and stack[-1] in '*/':
        x = stack.pop()
        a = stack.pop()
        stack.append(a * nums if x == '*' else a / nums)
    else:
        stack.append(nums)

    # 计算栈中最终值
    while len(stack) != 1:
        b = stack.pop()
        x = stack.pop()
        a = stack.pop()
        stack.append(a + b if x == '+' else a - b)
    
    return stack[0], i

print(func(str, 0)[0])

