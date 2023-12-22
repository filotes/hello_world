# 设计一个类(类比生活中：设计一张登记表)
class Student:
    name = None
    nationality = None
    gender = None
    age = None
    """
    类中定义的属性(变量)，我们称之为：成员变量
    类中定义的行为(函数)，我们称之为：成员方法
    """

    def say_hi(self):
        print(f"Hi大家好，我是{self.name}")


# 创建一个对象(类比生活中：打印一张登记表)


sut_1 = Student()
stu_2 = Student()

# 对象属性进行赋值(类比生活中：填写表单)
sut_1.name = "凌俊杰"
sut_1.gender = "男"
sut_1.nationality = "中国"
sut_1.age = 32

# 获取对象中记录的信息
print(sut_1.name)
print(sut_1.gender)
print(sut_1.nationality)
print(sut_1.age)

sut_1.say_hi()
