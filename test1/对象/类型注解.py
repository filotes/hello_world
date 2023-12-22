# 类型注解
# 支持：
# 变量的类型注解
# 函数(方法)形参列表和返回值的类型注解

# 基础数据类型注解
var1: int = 10
var2: float = 11.45
var3: bool = True
var4: str = "hanser"
var5 = "charlotte"


# 类对象类型注解


class Student:
    pass


stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3, 4, 5]
my_tuple: tuple = (1, 2, 3, 4, 5)
my_set: set = {1, 2, 3, 4, 5}
my_dict: dict = {"itheima": 666}
my_str: str = "hanser"

# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[str, int, bool] = ("hanser", 1145, True)
my_set: set[int] = {1, 2, 3}
my_dict: dict[str, int] = {"hanser": 114514}

import random
import json

random.randint(100, 200)

var_1 = random.randint(1, 10)  # type: int
var_1 = json.loads('{"name": "zhangshan"}')  # type: dict[str, str]


def func():
    return 10


var_3 = func()  # type: int

"""
为变量设置注释，显示的变量定义，一般无需注解
一般，无法直接看出变量类型之时会添加变量的类型注解
"""