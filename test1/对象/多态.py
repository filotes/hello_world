# 抽象类(接口)
class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_1_r(self):
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷核心科技")

    def hot_wind(self):
        print("美的空调加热")

    def swing_1_r(self):
        print("美的空调摆风")


class Gree_AC(AC):
    def cool_wind(self):
        print("格力空调制冷核心科技")

    def hot_wind(self):
        print("格力空调加热")

    def swing_1_r(self):
        print("格力空调摆风")


def make_cool(ac: AC):
    ac.cool_wind()


midea_ac = Midea_AC()
green_ac = Gree_AC()

make_cool(midea_ac)
make_cool(green_ac)
