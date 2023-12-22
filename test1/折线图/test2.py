from pyecharts.charts import Bar
from pyecharts.options import *
import random


def my_list(bars, xlists, ylists,  titlename):
    bars.add_xaxis(xlists)
    bars.add_yaxis(titlename, ylists, color=color(), label_opts=LabelOpts(position="right"))
    bars.reversal_axis()


def color():
    lis = ["red", "yellow", "green", "blue", "#00868B", "#FFFF00", "#90EE90"]
    num2 = random.randint(0, 6)
    sed = lis[num2]
    return sed


def num():
    i = 0
    me = []
    while i < 10:
        i += 1
        num1 = random.randint(100, 10000)
        me.append(num1)
    return me


def zid(name):
    my_list(name, ne, num(), "GDP趋势")


x = "11"
bar = "bar"
y = int(x)
while y < 100:
    y += 1

    x = str(y)
    bs = bar + x
    ba = Bar()
    zid(ba)
    print(bs)