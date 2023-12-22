# 捕获常规异常

"""
基本语法
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
"""
# import my_package.str_util

"""
try:
    f1 = open("E/file.txt.bak", "r", encoding="UTF-8")
except:
    f1 = open("E:/file.txt.bak", "w", encoding="UTF-8")

# 捕获指定异常
try:
    print(name)
except NameError as a:
    print(a)

# 捕获多个异常
try:
    print(1/0)
except (NameError, ZeroDivisionError) as b:
    print(b)
"""

# 捕获全部异常

# try:
#     print(name), 123456

# except Exception as c:
#     print(c)

"""
异常else
try:
print(1)
except Exception as e:
else:
    print("我是else，是没有异常的时候执行的代码")
"""
# finally表示的是无论是否异常都要执行的代码文件

"""
模块的导入方式
[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]    []内为非必填 *为模块的全部内容
import 模块名
from 模块名 import 类，变量，方法等，
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名
"""

# from time import sleep

# print(1)
# sleep(5)
# print(5)

# import time as t
# t.sleep(5)
# print(5)
# from time import sleep as s
# s(2)
# print(2)

# 自定义模块

# import mode
# mode.te(10, 20)
# # 当调用两个相同名称的模块，会使用后面调用的模块
# import mode2
# mode2.te1(1, 2)
# mode2.te2(1, 2)

# __all__变量可以控制*导入可以导入那些模块
# from MOD import *
# hi1(5, 5)
# hi2(5, 2)
# hi3(5, 5)

# 导入包
# import 包名.模块名
# 包名.模块名.目标

"""
导入包内的module
import my_package.module1
my_package.module1.info_print1(5, 5)
my_package.module1.info_print2(5, 5)

import my_package.module2
my_package.module2.info_print3(5, 5)
my_package.module2.info_print4(5, 5)
"""
