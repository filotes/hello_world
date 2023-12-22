# 元组定义：使用小括号，用逗号隔开，可以是不同的数据类型   tuple   无法修改
t1 = ((1, 2, 3), (4, 5, 6))
print(f"t1的类型是{type(t1)}")
v = t1[1][-1]
print(v)

sj = ("miku", 18, ["football", "music"])
nl = sj.index(18)
print(f"年龄的下标是{nl}")
xm = sj[0]
print(f"姓名是{xm}")
# sj[2] del [0]
del sj[2][0]
print(f"删除爱好football后是{sj}")
sj[2].insert(0, "codinf")
print(f"增加了codinf到list后是{sj}")

# 字符串   无法修改
str1 = "charlotte"
v1 = str1[0]
v2 = str1[-1]
print(f"从字符串str1取出下标为0的数是{v1}")
print(f"从字符串str1取出下标为-1的数是{v2}")

# replace会得到新的字符串
str2 = "charlotte"
str3 = str2.replace("char", "han")
print(str2)
print(str3)

# split(切割方式) 切割
str4 = "hanser charlotte miku"
f = str4.split(" ")
print(f)

"""
# 去除前后空格
字符串.strip()
# 取除前后指定的字符串
字符串.strip(字符串)
"""

my_str = "white"
# while循环
index = 0
while index < len(my_str):
    g = my_str[index]
    index += 1
    print(g)

# for循环
for x in my_str:
    print(x)

my_str = "itheima itcast boxuegu"
h_g = my_str.count("it")
print(f"字符串{my_str}中有{h_g}个it")
h_h = my_str.replace(" ", "|")
print(f"字符串{my_str}把空格换成|后是{h_h}")
g_g = h_h.split("|")
print(g_g)

"""
切片
序列是指：内容连续，有序，可以使用下标索引的一类数据容器
列表，元组，字符串，均可以视为序列
语法  序列[起始下标:结束下标:步长]
表示从序列中，从指定位置开始，依次取处元素，到指定位置结束，得到一个新序列：
起始下标表示从何处开始，可以留空，留空表示从头开始
结束下标(不含本身)表示何处结束，可以留空，留空视作截取到结尾
步长表示，依次取元素的间隔   默认是1    可以写负数(表示从后往前取)
步长N表示，每次跳过N-1个元素取
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = my_list[0:5]
print(num)
num = my_list[0:12:2]
print(num)
