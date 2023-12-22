# class Student:
#
#     def __init__(self, name, age, tile):
#         self.name = name
#         self.age = age
#         self.title = tile
#
#
# i = 1
# for x in "1234567890":
#     print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
#     name = input("请输入学生姓名：")
#     age = input("请输入学生年龄：")
#     tile = input("请输入学生地址：")
#     stu1 = Student(name, age, tile)
#     print(f"学生{i}信息录入完毕，信息为；【学生姓名：{stu1.name}, 年龄：{stu1.age}, 地址：{stu1.title}】")
#     i += 1


# class Student:
#
#     def __init__(self):
#         self.name = input("请输入学生姓名：")
#         self.age = input("请输入学生年龄：")
#         self.add = input("请输入学生地址：")
#
#
# for x in range(1, 11):
#     print(f"当前录入第{x}为学生信息，总共需录入10位学生信息")
#     stu = Student()
#     print(f"学生{x}信息录入完毕，信息为：【学生姓名：{stu.name}, 学生年龄：{stu.age}, 学生地址：{stu.add}】")

class Phone:
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G开启")
        else:
            print("5G关闭，使用4G网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone1 = Phone()
phone1.call_by_5g()
