# i = 1
# while i <= 100:
#     print(f"今天是第{i}天准备表白......")
#     j = 1
#     while j <= 10:
#         print(f"送给小美第{j}只玫瑰花")
#         j += 1
#     print("小美，我喜欢你！")
#     i += 1
# print(f"坚持到第{i}天，表白成功！")

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j} * {i} = {j * i}\t", end='')
#         j += 1
#     i += 1
#     print()
"""
money = int(5000000)


def ye():
    print("---------------查询余额---------------")
    print(f"{name}，您好，您的余额剩余:{money}")


def ck():
    print("----------------存款----------------")
    q = int(input("请输入您的存款数:"))
    global money     += q
    print("----------------存款----------------")
    print(f"{name}，您好，您存款{q}元\n{name}，您好，您的余额剩余{money}元")


def qk():
    print("----------------取款----------------")
    c = int(input("请输入您的取款数:"))
    global money     -= c
    print("----------------取款----------------")
    print(f"{name}，您好，您取款{c}元\n{name}，您好，您的余额剩余{money}元")


def js():
    print(f"再见{name},欢迎下次光临！")


name = input("请输入您的名字:")
while True:
    print("----------------主菜单----------------")
    print(f"{name},您好，欢迎来到罐头银行ATM，请选择操作:")
    print("查询余额\t [输入1]")
    print("存款\t     [输入2]")
    print("取款\t     [输入3]")
    print("退出\t     [输入4]")
    h = int(input("请输入:"))
    if h == 1:
        ye()
    elif h == 2:
        ck()
    elif h == 3:
        qk()
    elif h == 4:
        js()
        break
"""

"""
一个函数返回多个值
"""


def test_return(a, b, c):
    return a, b, c


x, y, z = test_return(100, "+", 200)
print(x)
print(y)
print(z)

# print(test_return())
# 关键字参数 可以和位置参数混用，但位置参数必须在前


def user_li(name, age, gender):
    print(f"姓名是:{name},年龄是{age},性别是{gender}")


user_li("蔡徐坤", 18, "鸡")
user_li("蔡徐坤", 19, gender="鸡")
user_li(name="蔡徐坤", age=18, gender="鸡")

# 缺省参数


def user_my(name, age, gender="武装直升机"):
    print(f"姓名是:{name},年龄是:{age},性别是:{gender}")
# 默认值必须在最后


user_my("TOm", "22", "cat")
user_my("TOm", "22")


def ans(*args):
    print(args)
# 所有参数都会被args收集，并合并成一个元组(tuple),args是元组类型，这就是位置传递


ans(1, 2, 3, 4, 5)

# 关键值传递
# 参数是 ”键=值“ 形式的情况下，所有的 ”键=值“ 都会被kwargs接收，同时会根据 ”键=值“ 组成字典
h = {}


def user_1(**kwargs):
    print(kwargs)
    global h
    h = kwargs
    # j = kwargs
    # print(j)


user_1(name="TOM", age="18", gender="cat")
print(h)
print(type(h))


# 函数作为参数传递
n = 5
k = 5



def test(compute):
    reset = compute(n, k)
    print(reset)


def compute(x, y):
    return x + y


test(compute)

# lambda匿名函数


def gi_hi(cont):
    gi = cont(1, 3)
    print(gi)


gi_hi(lambda x, y: x + y)

af = lambda x, y: x + y

gi_hi(af)
