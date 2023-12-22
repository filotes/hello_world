import json
from pyecharts.charts import Map
from pyecharts.options import *
# 打开文件
file1 = open("C:/疫情.txt", "r", encoding="UTF-8")
data = file1.read()
# 转换为json数据
data = json.loads(data)
# 取得children的数据
data = data["areaTree"][0]["children"]
# print(data)
lb = []         # 定义一个列表，装名称和人数
# for循环
for fi in data:
    s = "省"
    name = fi["name"]           # 省份名称
    rens = fi["total"]["confirm"]           # 人数
    for x in data:
        nam = x["name"] + "省"
        # map_data = map_data.insert(index, name + s)
        # print(type(name))
        # print(name)
        # name = str(name)
        # g = name + s
        # print(g)
        # nam = name.replace(name, g)
        # print(nam)
        lb.append((nam, rens))
print(lb)
d = data
# 创建地图对象
my_map2 = Map()
# 地图数据
map_data = lb
# 导入
my_map2.add("省份人数", map_data, "china")
# # 全局选项
my_map2.set_global_opts(
    title_opts=TitleOpts(title="各省人数", pos_left="center", pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(is_show=True
                                 ,
                                 is_piecewise=True,
                                 pieces=[
                                     {"min": 1, "max": 499, "label": "1-499人", "color": "#00F5FF"},
                                     {"min": 500, "max": 999, "label": "500-999人", "color": "#00868B"},
                                     {"min": 1000, "max": 3599, "label": "1000-3599人", "color": "#FFFF00"},
                                     {"min": 3600, "max": 5999, "label": "3600-5999人", "color": "#90EE90"},
                                     {"min": 6000, "max": 7999, "label": "6000-7999人", "color": "#FF0000"},
                                     {"min": 8000, "label": "8000+人", "color": "#8B0000"}
                                 ])      # color

)
# 生成地图
my_map2.render()
