"""
使用对象组织数据
"""


# 在程序中设计表格，我们称之为：设计类(class)
class Student:
    name = None                 # 记录姓名
    gender = None               # 记录性别
    nationality = None          # 记录国籍
    native_place = None         # 记录籍贯
    age = None                  # 记录年龄


# 在程序中打印生产表格，称之为：创建对象


sut_1 = Student()
sut_2 = Student()
# 在程序中填写表格，称之为：对象属性赋值

sut_1.name = "凌俊杰"
sut_2.name = "周杰伦"
print(Student)
print(sut_1)
print(sut_2)
