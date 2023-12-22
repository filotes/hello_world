
# class Clock:
#     id = None
#     price = None
#
#     def ring(self):
#         import winsound
#         # winsound.Beep(2000, 3000)
#
#
# clock1 = Clock()
# clock1.id = "114514"
# clock1.price = 9.9
# clock1.ring()

"""
构造方法
python类可以使用：__init__()方法，称之为构造方法
可以实现：
在创建类对象(构造类)的时候，会自动执行
在创建类对象(构造类)的时候，将传入参数自动传递给__init__()方法使用
"""


class Miku:
    """
    name = None
    age = None
    til = None
    用__init__可以不写
    """

    def __init__(self, name, age, til):
        self.name = name
        self.age = age
        self.til = til
        # 声明并且赋值


miku1 = Miku("蔡徐坤", "24", 114514)
print(miku1.name)
print(miku1.age)
print(miku1.til)
