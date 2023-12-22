"""
多行注释
"""
print("你好，世界")
print("Hello World")
# 写一个整数字面量
# 666
# 写一个浮点数字面量
# 13.14
# 写一个字符串字面量
"你好"
# 通过print语句输出各类字面量
print("666")
print("13.14")
print("你干嘛~哎呦")

# 定义一个变量
money = 50
# 通过print语句，输出变量的值
print("钱包还有:", money)
# 买了一个冰淇淋花费了10元
money = money - 10
print("买了一个冰淇淋花费了10元还剩:", money)
# 用逗号隔开，可以输出多个字符串
print("Hello World", "你好，世界")
# 假设，每隔一个小时，输出一下钱包余额
print("现在是下午一点：", money)
print("现在是下午二点：", money)
print("现在是下午三点：", money)
print("现在是下午四点：", money)
# 变量
test = 10
print("变量等于10")
test = test * 10
print("变量乘10：", test)
test = test / 10
print("变量除以10：", test)
test = test + 10
print("变量加10：", test)
b = 10
a = b
print(b)
# type语句的使用方式
# 整形
print(type(666))
# 字符串型
print(type("鸡你太美"))
# 浮点型
print(type(11.45))
# 用变量存储type的结果
string_type = type(114)
print(string_type)
# 用type查看变量中存储的数据类型
name = 1145
name_type = type(name)
print(name_type)
# 数据类型的转换
num_str = str(1145)
print(type(num_str), num_str)

float_str = str(12.34)
print(type(float_str), float_str)

num_int = int("123")
print(type(num_int), num_int)

num_float = float("123.456")
print(type(num_float), num_float)
# 想要将字符串转换成数字，必须要求字符串里的都是数字
# 整数转浮点数
q_float = float(11)
print(type(q_float), q_float)
# 浮点数转整数
w_int = int(10.921)
print(type(w_int), w_int)
"""
标识符
规则一：内容限定，只能用中文，英文，数字，下划线。 注意：不能以数字开头
规则二：大小写敏感 （可以识别大小写）
规则三：不可以使用关键字
"""
# 运算符
print("1 + 1 = ", 1 + 1)  # 加
print("2 - 1 = ", 2 - 1)  # 减
print("3 * 3 = ", 3 * 3)  # 乘
print("4 / 2 = ", 4 / 2)  # 除
print("9 // 2 = ", 9 // 2)  # 取整除
print("10 % 3 = ", 10 % 3)  # 取余
print("2 ** 3 = ", 2 ** 3)  # 指数（次方）
# 复合赋值运算
miku = 1
miku += 1  # += -+ *= /= //= %= **=
print("miku += 1:", miku)

print("\"qwerty")
test1 = """
 你
 干
 嘛
 ~
 哎
 呦
"""
print(test1)

# 字符串的拼接
we = "人生"
print(we + "苦短", "我用python")
wel_str = str(100)
print("有" + wel_str)

# 字符串格式化
bj = "22计网"
rs = 50
he = "%s班级，人数%s人" % (bj, rs)  # 多个变量占位，变量要用括号括起来，按顺序填入
print(he)
"""
其中的 %s
%表示：我要占位
s表示：将变量变成字符串放入占位的地方
"""
# %s    字符串         %d整数            %f浮点数
class_a = 2.5
class_b = "蔡徐坤"
class_c = 50
name_a = "我是练习时长%.1f年的练习生，我叫%s，我有%d万fans" % (class_a, class_b, class_c)
# %{}.()f ()里是几，就保留几位小数  {}是几，宽度就是几
print(name_a)
# f占位   format
name_word = "迪亚519"
house = 1145
fantasy = "大巴神"
print(f"我是{name_word},我今年{house}岁，我是个{fantasy}")
# 表达式   指的是有明确结果的代码语句
# 如何格式化表达式
# f"{}"
# %s\%d\%f(表达式)
print(f"3 * 3等于{3 * 3}")
name_ = "传智播客"
stock_price = 11.45
stock_code = "014514"
tis = 1.2
growth_days = 10
git = (stock_price * tis ** growth_days)
print(f"公司：{name_}，股票代码：{stock_code}，当前股价：%.2f" % stock_price)
print(f"每日增长系数是：%.1f，经过%d的增长后，股价达到了：{stock_price * tis ** growth_days}" % (tis, growth_days))
print("每日增长系数是：%.1f，经过%d的增长后，股价达到了：%.2f" % (tis, growth_days, git))

# hie = input("请告诉我你是谁?")
# print("我知道了，你是：%s" % hie)

# num = input("请告诉我你的银行卡密码")
# print("你的银行卡密码类型是：", type (num))
# num = int(num)
# print("你的银行卡密码类型是：", type (num))

# user_name = input("请输入您的名称")
# user_type = input("请输入您的用户类型")
# print(f"您好:{user_name},您是尊贵的：{user_type}用户，欢迎您的光临。")
# True真  False假
qi = 100 > 50
print(f"100大于50：{qi}", type(qi))

# 比较运算符
# ==    !=  >   <   >=  <=
bool_1 = 100 != 100
print(f"100!=100{bool_1}", type(bool_1))
bool_2 = int(20)
bool_3 = int(25)
print("20 <= 30的结果是:%s" % (bool_2 <= bool_3))
print(f"20 != 30的结果是:{bool_2 != bool_3}")

# print("欢迎来到乐土")
# age = float(input("请输入您的年龄:"))
# if age >= 18:
#     print("你是成年人，游玩需要10元。")
#     print("祝您游玩愉快")
# else:
#     print("你是未成年人，可免费畅玩。")
#     print("祝您游玩愉快")

# qi = input("请输入您的名字：")
# qi_2 = input("起输入您的性别")
#
# if qi == "张鹏华":
#     print("你是舔狗")
#
# elif qi == "刘志刚":
#     print("你是帅哥")
#
# elif qi == "王后祥":
#     print("你是SB")
#
# elif qi == "罗婧文":
#     print("你是蠢软")
#
# elif qi_2 == "男":
#     print("你是出生")
#
# elif qi_2 == "女":
#     print("你是出生")

# else:
#     print("你不是舔狗")#

# print("这是一个计算机(只能计算乘法！！！请先后输入！)")
#  set_option = float(input("请输入:"))
# set_in = float(input("请输入:"))
# set_on = set_option * set_in
# print(set_on)

# print("这是一个猜文字游戏，你有5次机会，范围50-100")
# if int(input("请输入第一次猜想的数字:")) == 75:
#     print("恭喜你猜对了！")
# elif int(input("错了蠢软，你还有4次机会！")) == 75:
#     print("恭喜你猜对了！")
# elif int(input("又错了傻逼，你还有3次机会！")) == 75:
#     print("恭喜你猜对了！")
# elif int(input("又又错了傻逼，你还有2次机会！")) == 75:
#     print("恭喜你猜对了！")
# elif int(input("又又又错了傻鸟，你还有1次机会！")) == 75:
#     print("恭喜你猜对了！")
# else:
#     print("你没机会了蠢软，我想的是75！傻狗！")

# e = float(input("请输入您的年龄:"))
# o = float(input("请输入您的入职时间:"))
# p = float(input("请输入您的级别:"))
# if e >= 18:
#     print("您是成年人")
#     if e < 30:
#         print("您的年龄达标了")
#         if o > 2:
#             print("您的年龄大于18，入职时间大于2年，可以免费领取！")
#         elif p > 3:
#             print("您的年龄大于18，及级别大于3，可以免费领取！")
#         else:
#             print("不好意思，您年龄虽然达标了，但入职时间和级别都不满足，不能领取")
#     else:
#         print("您的年龄大于30，不能领取")
# else:
#     print("您不满18，不能领取")

# 运算符
print("1 + 1 = ", 1 + 1)  # 加
print("2 - 1 = ", 2 - 1)  # 减
print("3 * 3 = ", 3 * 3)  # 乘
print("4 / 2 = ", 4 / 2)  # 除
print("9 // 2 = ", 9 // 2)  # 取整除
print("10 % 3 = ", 10 % 3)  # 取余
print("2 ** 3 = ", 2 ** 3)  # 指数（次方）
# 复合赋值运算
miku = 1
miku += 1  # += -+ *= /= //= %= **=
print("miku += 1:", miku)
