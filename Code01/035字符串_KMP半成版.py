# 无next实现步骤 KMP
# 模式串为 "PPDPPDPZ" 它的Next数组为[-1, 0, 1, 0, 1, 2, 3, 1]

def match(s1, s2, next):
    # 生成对应s2的Next; 暂时省略
    i = 0
    j = 0   # i是s1的下标变量，j是s2的下标变量

    # while i < len(s1):
    #     if s1[i] == s2[j]:  # 如果开始匹配前缀了
    #         while j != -1:  # 直到移动到模式串的开头
    #             while j < len(s2) and s1[i] == s2[j]:
    #                 i += 1
    #                 j += 1
    #             if j == len(s2):
    #                 return True
    #             j = next[j]
    #         j = 0   # 执行到此步 证明直到当前i之前的所有字符开头都配不出s2
    #     i += 1

    while i < len(s1):
        if s1[i] == s2[j]:
            i += 1
            j += 1
            if j == len(s2):
                return i - j    # j此时表示的是模式串的长度，只需要让i往回退j长度就能得到匹配串的起始位置
        else:
            j = next[j]
        if j == -1: # 执行到此步 证明直到当前i之前的所有字符开头都配不出s2
            j = 0
            i += 1
            
    return -1



if __name__ == '__main__':
    s1 = "aaaPPDPPDPwPPDPPDPPPDPPDPZ"
    s2 = "PPDPPDPZ"
    next = [-1, 0, 1, 0, 1, 2, 3, 4]

    r = match(s1, s2, next)
    if r == -1:
        print("不存在")
    else:
        print(f"s2在s1的{r}处")
    
