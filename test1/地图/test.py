import random

from pyecharts.charts import Bar, Timeline
from pyecharts.options import *


def my_list(bars, xlists, ylists,  titlename):
    bars.add_xaxis(xlists)
    bars.add_yaxis(titlename, ylists, color=color(), label_opts=LabelOpts(position="right"))
    bars.reversal_axis()
# bar1 = Bar()
# bar1.add_yaxis()
# bar1.reversal_axis()


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


# print(num())

bar1 = Bar()
my_list(bar1, ["江西", "上海", "深圳", "湖南", "广东", "北京", "安徽", "台湾", "璃月", "稻妻"], num(),
        "GDP趋势")

ne = ["江西", "上海", "深圳", "湖南", "广东", "北京", "安徽", "台湾", "璃月", "稻妻"]
bar2 = Bar()
my_list(bar2, ne, num(), "GDP趋势")
# bar1.render("test.html")

bar3 = Bar()
my_list(bar3, ne, num(), "GDP趋势")
timeline = Timeline()


def zid(name):
    my_list(name, ne, num(), "GDP趋势")


def time(bars, title):
    timeline.add(bars, title)


x = ["11"]
bar = "bar"
# while x < 100:
#     x = (f"{"bar"} + {x}")
#     x += 1
a = bar + x
print(a)
y = int(x)
while y < 100:
    y += 1

    x = str(y)
bar4 = Bar()
zid(bar4)

bar5 = Bar()
zid(bar5)

bar6 = Bar()
zid(bar6)

bar7 = Bar()
zid(bar7)

bar8 = Bar()
zid(bar8)

bar9 = Bar()
zid(bar9)

bar10 = Bar()
zid(bar10)

timeline.add_schema(
    play_interval=1000,
    is_inverse=True,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

time(bar1, "2014GDP趋势")
time(bar2, "2015GDP趋势")
time(bar3, "2016GDP趋势")
time(bar4, "2017GDP趋势")
time(bar5, "2018GDP趋势")
time(bar6, "2019GDP趋势")
time(bar7, "2020GDP趋势")
time(bar8, "2021GDP趋势")
time(bar9, "2022GDP趋势")
time(bar10, "2023GDP趋势")

timeline.render("test.html")
