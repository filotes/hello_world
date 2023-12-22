from pyecharts.charts import Line
from pyecharts.options import *
import json
# 处理数据
f_us = open("C:/美国.txt", "r", encoding="UTF-8")
f_jp = open("C:/日本.txt", "r", encoding="UTF-8")
f_yd = open("C:/印度.txt", "r", encoding="UTF-8")
# 读取文件
us_data = f_us.read()       # 美国的内容
jp_data = f_jp.read()       # 日本的内容
yd_data = f_yd.read()       # 印度的内容
# 去除开头不规范的内容
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
yd_data = yd_data.replace("jsonp_1629350745930_63180(", "")
# 去除结尾不标准的内容
us_data = us_data[:-2]
jp_data = jp_data[:-2]
yd_data = yd_data[:-2]
# json转为字典
us_data = json.loads(us_data)
jp_data = json.loads(jp_data)
yd_data = json.loads(yd_data)
# 获取updateDate的内容，用于x轴
us_x_data = us_data["data"][0]["trend"]["updateDate"]
jp_x_data = jp_data["data"][0]["trend"]["updateDate"]
yd_x_data = yd_data["data"][0]["trend"]["updateDate"]
# 获取到第313位
us_x_data = us_x_data[:314]
jp_x_data = jp_x_data[:314]
yd_x_data = yd_x_data[:314]
# 获取data的内容，用于y轴
us_y_data = us_data["data"][0]["trend"]["list"][0]["data"][:314]
jp_y_data = jp_data["data"][0]["trend"]["list"][0]["data"][:314]
yd_y_data = yd_data["data"][0]["trend"]["list"][0]["data"][:314]
# print(us_x_data)
# print(us_y_data)

# 生成图表
my_map = Line()
# 添加x轴数据
my_map.add_xaxis(us_x_data)
# 添加y轴数据
my_map.add_yaxis("美国确诊人数", us_y_data, label_opts=LegendOpts(is_show=False), color="blue")  # 图例，是否显示y轴数据
my_map.add_yaxis("日本确诊人数", jp_y_data, label_opts=LegendOpts(is_show=False), color="red")
my_map.add_yaxis("印度确诊人数", yd_y_data, label_opts=LegendOpts(is_show=False), color="green")
# 设置全局配置
my_map.set_global_opts(     # 标题设置
    title_opts=TitleOpts(title="美国，日本，印度三国疫情确诊人数折线图", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    # visualmap_opts=VisualMapOpts(is_show=True)
)
# 调用render，生成图表
my_map.render()
# 关闭文件
f_us.close()
f_jp.close()
f_yd.close()
