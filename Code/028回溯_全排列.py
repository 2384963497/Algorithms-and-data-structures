# 输出ABCDE的全排列

def func(str):
    global count
    if len(str) == len(l):
        print(str)
        count += 1
        return
    for i in l:
        if i not in str:
            func(str+i)

if __name__ == '__main__':
    count = 0
    l = ['A', 'B', 'C', 'D', 'E']
    func('')
    print(count)
