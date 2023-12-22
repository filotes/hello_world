# 计算机编码
"""
UTF-8
GBK
Big5
等
"""
# import time

# import time

# 读取文件方法
"""
read()方法:
文件对象:read(num)      num表示要从文件中读取的数据长度(单位是字节)，如果没有传入num，就表示读取全部内容

"""
# mod常用的三总模式    r(只读)     w(写入)     a(追加)

# f = open("C:/PyCharm/test.txt", "r", encoding="UTF-8")
# print(f.read(5))
# print(f.read())

# readlines()方法     读取文件的全部行，封装到列表中

# lis = f.readlines()
# print(f"lis的类型是:{type(lis)}")
# print(f"lis的内容是:{lis}")

# readline()方法      一次读取一行内容

# gi1 = f.readline()
# print(f"第一行的内容是:{gi1}")

# for循环读取文件，一次读取一行
# 每一个临时变量就记录了一行数据
# g = 1
# for lin in f:
#     print(f"第{g}行的内容是:{lin}")
#     g += 1

# 暂停10秒     time.sleep(10)

# 文件的关闭
# 文件名.close()
# f.close()

"""
with open 语法
with open(文件路径，打开方式，编码格式) as 名称:
with open("C:/PyCharm/test.txt", "r", encoding="UTF-8") as nm:
    ad = 1
    for ig in nm:
        print(f"第{ad}行的内容是:{ig}")
        ad += 1         # 运行完后自动关闭文件

time.sleep(100)
"""

# f = open("C:/PyCharm/test2.txt", "r", encoding="UTF-8")
#
# gh = f.readlines()
# # f.close()
# print(gh)
# j = 0
# if gh == "itheima":
#     j += 1
# print(j)
# jl = gh.split("")

"""
w = open("C:/PyCharm/test2.txt", "r", encoding="UTF-8")
g = w.read()
h = g.count("itheima")
print(h)

w.close()

w = open("C:/PyCharm/test2.txt", "r", encoding="UTF-8")

h = 0
for line in w:
    line = line.strip()
    f = line.split(" ")
    for x in f:
        if x == "itheima":
            h += 1
print(h)

w.close()
"""

# 写入文件(内存)      file.write(数据)
# 内容刷新(硬盘)      file.flush()

# 打开不存在的文件
# f = open("C:/ikun.txt", "w", encoding="UTF-8")
# f.write("Hello Word")       # 写入内存
# f.flush()                   # 写入硬盘
# time.sleep(1000)
# f.close()           # close内置了flush的方法

# 当文件存在，w写入会吧文件内容清空
# 当文件不存在，w写入会创建新文件

# f = open("C:/ikun.txt", "a", encoding="UTF-8")
#
# f.write("\n鸡你太美")
# f.close()
# f = open("C:/ikun.txt", "a", encoding="UTF-8")
#
# f.write("\n1145141919810")
# f.close()

fr = open("C:/file.txt", "r", encoding="UTF-8")
fw = open("C:/file2.txt", "w", encoding="UTF-8")
for line in fr:
    line = line.strip()
    if line.split("，")[-1] == "测试":
        continue
    else:
        fw.write(line)
        fw.write("\n")
fr.close()
fw.close()
