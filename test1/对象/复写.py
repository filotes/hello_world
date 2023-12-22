class Phone:
    IMEI = None
    producer = "ITL"

    def call_by_5G(self):
        print("使用5G网络进行通话")

    def __memory(self):
        print("清理进程")


class new(Phone):
    producer = "ITZG"  # 复写父类的成员属性

    def call_by_5G(self):
        print("子项的5G通话")
        Phone.call_by_5G(self)
        print(f"父类的厂商是{super().producer}")
        super().call_by_5G()

    def __memory(self):
        print("结束进程")


# 调用父类重名成员

"""
方式1
*调用父类成员
使用成员变量：父类名.成员变量
使用成员方法：父类名.成员方法(self)

方式2
*使用super()调用父类成员
使用成员变量：super().成员变量
使用成员方法：super().成员方法()
"""

p = new()
p.call_by_5G()
print(p.producer)
print(Phone.producer)
