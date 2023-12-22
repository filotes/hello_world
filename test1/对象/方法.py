class Miku:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # str魔术方法,类对象转换为字符串
    def __str__(self):
        return f"Miku类对象，name={self.name},age={self.age}"

    # lt魔术方法，小于(大于)符号比较方法
    def __lt__(self, other):
        return self.age < other.age

    # le魔术方法，可用于<=,>=两种
    def __le__(self, other):
        return self.age <= other.age

    # eq魔术方法，可用于等于比较
    def __eq__(self, other):
        return self.age == other.age


fan1 = Miku("蔡徐坤", 24)
fan2 = Miku("周杰伦", 48)
fan3 = Miku("凌俊杰", 24)
print(fan1 > fan2)
print(fan1 < fan2)
print(fan1 >= fan2)
print(fan1 <= fan2)
print(fan1 >= fan3)
print(fan1 <= fan3)
print(fan1 == fan3)


# print(fan)
# print(str(fan))
