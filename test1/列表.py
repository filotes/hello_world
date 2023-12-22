# st = 1
# while st <= 9:
#     vi = 1
#     while vi <= st:
#         print(f"{vi} * {st} = {vi * st}\t", end='')
#         vi += 1
#     st += 1
#     print()
# from main import gi

# for i in range(1, 10):
#     for h in range(1, i + 1):
#         print(f"{h} * {i} = {h * i}\t", end='')
#     print()

# import random
# moni = 10000
# for v in range(1, 21):
#     g = random.randint(1, 10)
#     if g < 5:
#         print(f"员工{v}，绩效分{g}，低于5，不发工资，下一位！")
#         continue
#     elif moni >= 1000:
#         moni -= 1000
#         print(f"向员工{v}发放工资1000元，账户余额还剩{moni}元!")
#     else:
#         print(f"工资发完了，下个月领取吧！")
#         break
# str1 = "123"
# str2 = "123456"
# str3 = "123456789"

# gi = 0
# for er in str3:
#     gi += 1
# print(gi)

# 函数    组织好的，可重复使用的，用来实现特定功能的代码段

# def hi(da):
#     c = 0
#     for _ in da:
#         c += 1
#     print(c)
#
#
# hi(str1)
# hi(str2)
# hi(str3)

# def my_len():
#     print("欢迎来到提瓦特!\n请出示您的健康码以及72小时核酸证明!")
#
#
# my_len()

# a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a1[0])
# print(a1[1])
# print(a1[2])
# print(a1[3])
# print(a1[4])
# print(a1[5])
# if a1[0] == 1:
#     print(666)
# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
# my_list = [[a, b, c, d, e], [e, d, c, b, a]]
# print(my_list[1][1])
# print(my_list[0][3])
#
# class git:
#     def add(self, x, y):
#         return x + y

# 列表.index(元素)  查找指定元素在列表的下标
"""
mylist = ["jntm", "nmjj", "ngm"]
修改下标的值
mylist[0] = "jtm"
print(mylist)
"""
# insert(下标，元素) 插入元素
# mylist.insert(1, "鸡你太美")
# print(mylist)
"""
append(元素)    追加元素，将指定的元素追加到列表的尾部
mylist.append("你干嘛")
print(mylist)
mylist.insert(-1, "你干嘛")
print(mylist)
"""

# extend(其他数据容器)    将其他数据容器的内容取出，依次追加到列表尾部
# mylist.extend([1, 2, 3, 4, 5])
# print(f"追加了之后是{mylist}")

"""
删除指定下标索引的元素
语法1：del列表[下标]
语法2：列表.pop(下标)
mylist = [[1, 1, 4, 5, 1, 4], [1, 2, 3, 4, 5, 6]]
del mylist[1][5]
print(f"删除下标1, 5后是{mylist}")
h = mylist.pop(1)
print(f"删除下标1后是{mylist}")
"""


# 列表.remove(元素) 删除某元素在列表中的第一个匹配项，从前往后查找
# mylist = [1, 2, 3, 3, 4, 5]
# mylist.remove(3)
# print(f"删除元素3后结果是{mylist}")


"""
清空整个列表    列表.clear()
mylist = [1, 2, 3, 3, 4, 5]
mylist.clear()
print(mylist)
"""


# 统计某个元素在列表里的数量 列表.count(元素)
# mylist = [1, 1, 1, 2, 3, 4, 5]
# hg = mylist.count(1)
# print(f"列表中1的数量是{hg}")
# print(f"列表中1的数量是{mylist.count(1)}")

"""
len   统计列表内有多少个元素
mylist = [1, 1, 1, 2, 3, 4, 5]
hj = len(mylist)
print(f"列表中有{hj}个元素")
"""

# 列表的特点
# 1 可以容纳多个元素(上限为2**63-1个)
# 2 可以容纳不同类型的元素(混装)
# 3 数据是有序存储的(有下标序号)
# 4 允许重复数据存在
# 5 可以修改(增加或者删除元素等)


"""
nl = [21, 25, 21, 23, 22, 20]
print(f"初始列表是{nl}")
nl.append(31)
print(f"在列表{nl}最后追加31后为{nl}")
cl = [29, 33, 30]
nl.extend(cl)
print(f"追加新列表{cl}后是{nl}")
dy = nl[0]
print(f"取出列表{nl}第一个元素是{dy}")
zh = nl[-1]
print(f"取出列表{nl}最后一个元素是{zh}")
xb = nl.index(31)
print(f"列表{nl}元素31在列表下标位置{xb}")
"""

# while循环对列表的遍历

# h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f"列表是{h}")
# j = 0
# # j = int(j)
# # hj = len(h)
# # while j < hj:
# #     de = h[j]
# #     print(f"列表的元素{de}")
# #     j += 1

# for循环对列表的遍历

# ji = [1, 1, 4, 5, 1, 4]
# for x in ji:
#     print(f"列表的元素{x}")
