# 要求通过input()函数输入元素来创建一个长度为3的列表ls1，列表中所有元素均为整数。
# 将ls1中的每一个元素乘以2得到列表ls2，
# 然后将两个列表中对应位置元素相加得到一个新的列表 new_ls，打印输出新列表new_ls。


ls1 = []

for i in range(3):
    ls1.append(int(input(f"请输入与ls1的第{i+1}个值: ")))
ls2 = [i*2 for i in ls1]
print(f"ls2的元素为:{ls2}")
new_ls = [i+j for i,j in (ls1,ls2)]
# for i in range(len(ls1)):
#     new_ls.append(ls1[i]+ls2[i])
print(f"new_ls的元素为:{new_ls}")


# t = [i+j for i,j in ()]
# print(t)