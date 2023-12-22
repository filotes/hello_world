# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


# def print_hi(name):
# 在下面的代码行中使用断点来调试脚本。
# print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
# qi = input("请输入您的名字：")
#
# if qi == "张鹏华":
#     print("你是舔狗")
#
# elif qi == "王后祥":
#     print("你是SB")
#
# elif qi == "罗婧文":
#     print("你是蠢软")
#
# else:
#     print("你不是舔狗")

# i = 0
# te = True
# while te:
#     print("你是SB")
#     i += 1
#     if i == 100:
#         te = False
# di = 0
# tes = 50
# de = True
# while de:
#     di += tes
#     tes += 1
#     if tes > 1000:
#         de = False
# print(f"50-1000加起来的值是:{di}")
#
# di = 0
# tes = 50
# while tes <= 1000:
#     di += tes
#     tes += 1
# print(f"50-1000加起来的值是:{di}")

import random
num = random.randint(50, 100)
print("这是一个猜文字游戏，你有5次机会，范围50-100")
gi = 0
ig = True
while gi < 5:
    on = float(input("请输入您猜的数字:"))
    gi += 1
    if on == num:
        print("恭喜你猜对了！")
    else:
        if on > num:
            print("蠢软，大了")
        else:
            print("蠢软，小了")
print("你没机会了傻狗！")
