from pyecharts.charts import Bar, Timeline
from pyecharts.options import *

# ANSI表示系统的默认编码
# 默认中文编码GB2312
f = open("C:/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
# readlines得到的是一个列表
data = f.readlines()
# print(data)
print(type(data))
f.close()
data.pop(0)
# print(data)
dict_1 = {}
# 将数据转换为字典,Key=年份,Value=国家和GDP
for line in data:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])     # 科学计数法可以用float强制转换
    try:
        dict_1[year].append((country, gdp))
    except KeyError:
        dict_1[year] = []
        dict_1[year].append((country, gdp))

# 排序年份
sorted_year_list = sorted(dict_1.keys())
# print(sorted_year_list)
# print(dict_1)
# 创建时间线对象
# 设置主题
# timeline = Timeline({"theme": ThemeType.LIGHT})
timeline = Timeline()
for years in dict_1:
    dict_1[years].sort(key=lambda e: e[1], reverse=True)
    # 取出本年份前8的国家
    year_data = dict_1[years][0:8]
    # print(year_data)
    x_data = []
    y_data = []
    for x in year_data:
        x_data.append(x[0])     # x轴添加国家
        y_data.append(x[1] / 100000000)     # y轴添加GDP
    # print(x_data)
    # print(y_data)
    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    # if x_data == "中国":
    #     bar.add_xaxis(["中国"])
    #     bar.add_yaxis("GDP(亿)", y_data, color="red", label_opts=LabelOpts(position="right"))
    #     continue
    # print(x_data)
    # if x_data.count("中国") == 1:
    #     x_data.remove("中国")
    #     bar.add_xaxis("中国")
    #     bar.add_yaxis("GDP(亿)", y_data, color="ren", label_opts=LabelOpts(position="right"))
    #     continue
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # print(x_data)
    # 反转x和y轴
    bar.reversal_axis()
    # 设置每一年的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{years}年全国前8GDP数据")
    )

    timeline.add(bar, str(years))


timeline.add_schema(
            play_interval=1500,
            is_timeline_show=True,
            is_loop_play=True,
            is_auto_play=True
        )

timeline.render("1960-2019全球GDP前8国家.html")
