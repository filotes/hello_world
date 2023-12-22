# 私有对象前加__
# 私有对象只能在内部使用
class Phone:
    __current_voltage = None

    def __keep_memory(self):
        print("让CPU以单核模式运行")

    def call_by_5G(self):
        if self.__current_voltage >= 1:
            print("5G通话已开启")
        else:
            self.__keep_memory()
            print("电量不足，无法使用5G")


phone1 = Phone
phone1.call_by_5G()