from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
import random


def name(my_list, maxnum, kaishi, jieshu):
    """
    :param my_list: name
    :param maxnum: 最大多少个
    :param kaishi: 开始的数
    :param jieshu: 结束的数
    :return: 开始和结束之内的随机数
    """
    while len(my_list) < maxnum:
        a = random.randint(kaishi, jieshu)
        my_list.append(a)


def my_bar(my_name, my_list):
    """
    :param my_name: name
    :param my_list: y轴数据
    :return: Bar的x和y轴的数据，并把图表x和y轴反转
    """
    my_name.add_xaxis(["中国", "美国", "日本", "英国", "俄罗斯", "印度"])
    my_name.add_yaxis("GDP年度变化", my_list, color=color(),  label_opts=LabelOpts(position="right"))
    my_name.reversal_axis()


def color():
    """
    :return: 随机的颜色
    """
    colors = ["#00868B", "#90EE90", "#FFFF00", "#FF0000"]
    num = random.randint(0, 3)
    return colors[num]


# 定义一个空timeline时间轴
timeline = Timeline()

# 定义一个存储时间的空列表
lis = []

aa = 1982
b = 1
# while循环得到1983-2023年
while aa < 2023:
    aa += b
    lis.append(aa)

i = "1"
ae = "a"
ii = 1

# 定义一个空的列表,存储Bar的数据
c = []
while ii < 42:
    ae = ae + i
    c.append(ae)
    ii += 1
nem = []
ce = []
na = "GDP趋势"
# for循环的到y轴的GDP数据
for x2 in c:
    ce.append(x2)
# for循环得到1983年-2023年都加上GDP趋势的数据列表
for x in lis:
    x = str(x)
    x = x + na
    nem.append(x)

# print(nem)
ee = 0
# 把Bar的数据分别添加到timeline中,并通过下标取得年度
for x3 in ce:
    x3 = []
    x4 = x3
    name(x3, 6, 30000, 300000)
    ce = Bar()
    my_bar(ce, x4)
    timeline.add(ce, nem[ee])
    ee += 1

# 设置柱状图自动播放
timeline.add_schema(
    play_interval=1500,     # 自动播放间隔,单位毫秒
    is_timeline_show=True,  # 是否在自动播放的时候显示时间线
    is_auto_play=True,      # 是否自动播放
    is_loop_play=True       # 是否循环播放
)
# 生成图表
timeline.render("流动时间柱状图.html")
