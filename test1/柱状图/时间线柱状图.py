from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
import random


def num(my_lists, nummax, qishi, jieshu):
    s = 0
    while s < nummax:
        s = len(my_lists)
        my_num = random.randint(qishi, jieshu)
        my_lists.append(my_num)


ma = []
num(ma, 100, 100, 10000)
# while len(ma) < 100:
#     num = random.randint(100, 5000)
#     ma.append(num)

me = []
num(me, 100, 1000, 50000)
# while len(me) < 100:
#     num1 = random.randint(100, 10000)
#     me.append(num1)

# print(ma)
# print(me)
bar1 = Bar()

bar1.add_xaxis(["中国", "日本", "美国", "英国"])

bar1.add_yaxis("GDP", ma, color="#00868B", label_opts=LabelOpts(position="right"))

bar1.reversal_axis()

bar2 = Bar()

bar2.add_xaxis(["中国", "日本", "美国", "英国"])

bar2.add_yaxis("GDP", me, label_opts=LabelOpts(position="right"))

bar2.reversal_axis()

timeline = Timeline()

bar1.reversal_axis()
bar2.reversal_axis()

# timeline.add(bar1, "2022年GDP走向")
# timeline.add(bar2, "2023年GDP走向")


def time(name, title):
    timeline.add(name, title)


time(bar1, "2022年GDP趋势")
time(bar2, "2023年GDP趋势")
timeline.render("时间线柱状图.html")
