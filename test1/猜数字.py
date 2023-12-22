import random

num = random.randint(50, 100)
print("这是一个猜文字游戏，你有5次机会，范围50-100")
on = float(input("你还有5次机会，请输入你猜的数字:"))
if on == num:
    print("恭喜你一次就猜对了！")
else:
    if on > num:
        print("蠢软，大了")
    else:
        print("蠢软，小了")
    on = float(input("傻狗你还有4次机会:"))
    if on == num:
        print("恭喜你第二次就猜对了！")
    else:
        if on > num:
            print("傻鸟，大了")
        else:
            print("傻鸟，小了")
        on = float(input("傻逼你还有3次机会:"))
        if on == num:
            print("恭喜你第三次就猜对了！")
        else:
            if on > num:
                print("傻软，大了")
            else:
                print("傻软，小了")
            on = float(input("蠢狗你还有2次机会:"))
            if on == num:
                print("恭喜你第四次就猜对了！")
            else:
                if on > num:
                    print("SB，大了")
                else:
                    print("SB，小了")
                on = float(input("辣鸡你还就还有最后1次机会:"))
                if on == num:
                    print("恭喜你最后一次机会答对了！！！")
                else:
                    print("哈哈大蠢软，你没有机会了！！！")
                print(f"我的数字是{num}")

# 无限次机会猜数字

# import random
#
# shi = random.randint(1, 100)
# sf = 0
# mod = True
# while mod:
#     u = float(input("你有无数次机会，请输入你猜的数字:"))
#     sf += 1
#     if u == shi:
#         print("恭喜你猜对了！")
#         mod = False
#     else:
#         if u > shi:
#             print("大了")
#         else:
#             print("小了")
# print(f"您试了:{sf}次")
