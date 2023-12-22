import json
from pyecharts.charts import Map
from pyecharts.options import *
f = open("C:/疫情.txt", 'r', encoding="UTF-8")
f = f.read()
f = json.loads(f)
f = f["areaTree"][0]["children"][3]["children"]
# print(f)
data_list = []
for data in f:
    name = data["name"] + "市"
    da = data["total"]["confirm"]
    data_list.append((name, da))

print(data_list)
data_list.append(("济源市", 299))
my_map3 = Map()

my_map3.add("河南人数", data_list, "河南")

my_map3.set_global_opts(
    title_opts=TitleOpts(title="各省人数", pos_left="center", pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(is_show=True
                                 ,
                                 is_piecewise=True,
                                 pieces=[
                                     {"min": 1, "max": 9, "label": "1-9人", "color": "#00F5FF"},
                                     {"min": 10, "max": 99, "label": "10-99人", "color": "#00868B"},
                                     {"min": 100, "max": 199, "label": "100-199人", "color": "#FFFF00"},
                                     {"min": 200, "max": 299, "label": "200-299人", "color": "#90EE90"},
                                     {"min": 300, "max": 399, "label": "300-399人", "color": "#FF0000"},
                                 ])      # color

)

my_map3.render("河南.html")
