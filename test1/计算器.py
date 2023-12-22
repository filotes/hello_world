print("这是一个简易计算器，可以运算加(+),减(-),乘(*),除(/),次方(**),取余(%),取整除(//)")
print("输入exit退出！")
i = True
while i:
    gi = input("请输入第一个数：")
    if gi == "exit":
        break
    go = input("请输入运算符号:")
    if go == "exit":
        break
    gp = input("请输入第二个数:")
    if gp == "exit":
        break
    if go == '+':
        gi = float(gi)
        gp = float(gp)
        print(f"{gi}+{gp}={gi + gp}")
    elif go == '-':
        gi = float(gi)
        gp = float(gp)
        print(f"{gi}-{gp}={gi - gp}")
    elif go == '*':
        gi = float(gi)
        gp = float(gp)
        print(f"{gi}x{gp}={gi * gp}")
    elif go == '/':
        gi = float(gi)
        gp = float(gp)
        print(f"{gi}/{gp}={gi / gp}")
    elif go == '**':
        gi = float(gi)
        gp = float(gp)
        print(f"{gi}**{gp}={gi ** gp}")
    elif go == '%':
        gi = float(gi)
        gp = float(gp)
        print(f"{gi}%{gp}={gi % gp}")
    elif go == '//':
        gi = float(gi)
        gp = float(gp)
        print(f"{gi}//{gp}={gi // gp}")
    else:
        print("您的输入无效，请重新输入!")
