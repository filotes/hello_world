# for 循环
# for (临时变量) in (被统计的数据)
# o = "鸡你太美"
# for g in o:
#     print(g)

# name = "itheima is a brand of litcast"
# i = 0
# for x in name:
#     if x == "a":
#         i += 1
# print(f"itheima is a brand of litcast里有{i}个a")
# range
# range(num) 假设num=10 输出0-9 默认从0开始
# range(num1,num2) 假设num1=5 num2=10 输出5-9
# range(num1,num2,step) 假设num1=5 num2=10 step=2 输出5，7，9 step表示数值之间的间隔
# i = 0
# for g in range(10):
#     print("鸡你太美")
#     i += 1
# print(f"共输出{i}次")
# num = 100
# num = int(num)
# o = 0
# for g in range(1, 100):
#     if g % 2 == 0:
#         o += 1
# print(o)
# t = 0
# for t in range(5):
#     print(t)
# print(t)
# i = 1
# for i in range(i, 101):
#     print(f"今天是表白小美的第{i}天,加油!")
#     for j in range(1, 11):
#         print(f"这是送给小美的第{j}朵花")
#     print("小美我喜欢你!")
# print(f"坚持{i}天,表白成功!")
# for o in range(1, 10):
#     for i in range(1, 10):
#         print(f"{i} * {o} = {i * o}\t", end='')
#     print()
# for o in range(1, 10):
#     for i in range(1, o+1):
#         print(f"{i} * {o} = {i * o}\t", end='')
#     print()
# import random
# h = 10000
# for i in range(1, 21):
#     gz = random.randint(1, 10)
#     if gz < 5:
#         print(f"员工{i},绩效分{gz},低于5,不发工资,下一位")
#         continue
#     elif gz > 5:
#         print(f"向员工{i}发放工资1000元,账户余额还剩{h - 1000}")
#         h -= 1000
#         if h == 0:
#             print(f"帐户余额还剩0元,工资发完了,下个月领取吧!")
#             break
# g = 100
#
#
# def he():
#     print(f"test{g}")
#
#
# def he2():
#     # global g      全局变量global
#     g = 200
#     print(f"test{g}")
#
#
# he()
# he2()
# print(g)
"""
列表的遍历:

While遍历：
Name = 0		name(下标)
While name < len(列表):
    元素 = 列表[name]
    Name += 1

for循环:
for 临时变量 in 数据容器
    处理
"""

lebiao = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wkon = []
fkon = []
g = lebiao[-1]
# print(g)
f = 0
while f < len(lebiao):
    c = lebiao[f]
    f += 1
    if c % 2 == 0:
        wkon.append(c)
print(f"列表{lebiao}中偶数是{wkon}")
for x in lebiao:
    if x % 2 == 0:
        fkon.append(x)
print(f"列表{lebiao}中偶数是{fkon}")
