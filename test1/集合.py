str1 = "万过月薪 员序程马黑来 nohtyp学"
# a1 = str1.index("黑")
# a2 = str1.index("马")
# a3 = str1.index("程")
# a4 = str1.index("序")
# a5 = str1.index("员")
# b1 = str1[a1]
# b2 = str1[a2]
# b3 = str1[a3]
# b4 = str1[a4]
# b5 = str1[a5]
# print(b1 + b2 + b3 + b4 + b5)
f1 = str1.index("黑")
f2 = str1.index("员")
print(f1)
print(f2)
my_g = str1[f1:f2-1:-1]
print(my_g)
# fg = str1[::-1]
# print(fg)

"""
集合的特点
不允许重复，乱序
可以容纳多个数据
数据是无序存储的(不支持下标索引)
不允许重复数据
可以修改
支持for
"""

"""
集合的定义   
列表使用：   []
元组使用：   ()
字符串使用：  ""
集合使用：   {}
定义空集合   变量名 =  set()
"""
# 空集合 变量 = set()

my_set = {"hanser", "charlotte", "miku"}
print(f"my_set的内容是{my_set}, 类型是：{type(my_set)}")

# 添加元素
# 语法：   集合.add(元素)
my_set.add("kami")
print(f"my_set添加kami后是：{my_set}")

# 移除元素
# 语法：   集合.remove(元素)
my_set.remove("hanser")
print(f"my_set移除hanser后是：{my_set}")

# 随机取出元素
# 语法：   集合.pop()
my_set = {"hanser", "charlotte", "miku"}
Mi = my_set.pop()
print(f"取出的元素是{Mi}, 取完后还有{my_set}")

# 清空集合
# 语法：   集合.clear()
my_set = {"hanser", "charlotte", "miku"}
my_set.clear()
print(my_set)

# 取出两个集合的差集
# 语法：   集合1.difference(集合2)：取出集合一和集合二的差集(集合1有二集合二没得)    去完后原集合不变
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6, 7}
g = s1.difference(s2)
print(g)

# 消除两个集合的差集
# 语法：   集合1.difference_update(集合2)  对比集合1和集合2，在集合1内，删除和集合2相同的元素
# 结果    集合1被修改，集合2不变
s1 = {1, 3, 5, 7, 9}
s2 = {1, 2, 3, 4, 5}
s1.difference_update(s2)
print(f"消除集合1和集合2的差集后是{s1}")
print(f"集合s2是{s2}")

# 两集合合并
# 语法：   集合1.union(集合2)  功能：    将集合1和集合2组合成新集合   结果： 得到新集合，集合2和集合2不变
sw1 = {1, 2, 3, 4, 5, 6}
sw2 = {1, 3, 5, 7}
sw3 = sw1.union(sw2)
print(f"sw1和sw2组成新集合后是{sw3}")

# 统计集合元素个数
sw5 = {1, 2, 3, 4, 5}
num = len(sw5)
print(f"sw5中的元素有{num}个")
sw5 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
num1 = len(sw5)
print(f"sw5中的元素有{num1}个")       # 去重
sw5 = {1, 2, 3, 4, 5}
sw6 = set()
for x in sw5:
    sw6.add(x)
print(sw6)


set1 = set()
my_list = ["黑马程序员", "传智播客", "黑马程序员", "传智播客", "itheima", "itcast", "itheima", "itcast"]
for x in my_list:
    set1.add(x)
print(f"添加元素后set1为{set1}")
