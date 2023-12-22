# 单继承
# class 类名(父类名):
#     类体内容
class Phone:
    IMEI = None
    producer =None

    def call_by_4g(self):
        print("4G通话")


class Phone2023(Phone):
    face_id = True

    def call_by_5g(self):
        print("2023最新5G通话")


"""
多继承
class 类名(父类1, 父类2, 父类3......)
    类内内容
多继承注意事项
多个父类中,如果有同名成员,那么默认以继承顺序(从左到右)为优先级
即:先继承的被保留,后继承的被覆盖
"""


class NFCReader:
    nfc_type = "第五代"
    producer = "ZG"

    def read_card(self):
        print("读卡NFC")

    def write_card(self):
        print("写入NFC卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启")


class MyPhone(Phone, Phone2023, NFCReader, RemoteControl):
    pass
