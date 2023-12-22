from pyecharts.charts import Map
from pyecharts.options import *
# from pyecharts.options import VisualMapOpts
my_map = Map()

data = [
    ("北京省", 9),
    ("上海省", 99),
    ("湖南省", 199),
    ("台湾省", 299),
    ("广州省", 399),
    ("安徽省", 499),
    ("湖北省", 599),
    ("江西省", 699),
]

my_map.add("地图", data, "china")
# 地图设置
my_map.set_global_opts(
    visualmap_opts=VisualMapOpts(is_show=True, is_piecewise=True,
                                 pieces=[
                                     {"min": 1, "max": 9, "label": "1-9人", "color": "#00F5FF"},
                                     {"min": 10, "max": 99, "label": "10-99人", "color": "#00868B"},
                                     {"min": 100, "max": 199, "label": "100-199人", "color": "#FFFF00"},
                                     {"min": 200, "max": 399, "label": "200-399人", "color": "#90EE90"},
                                     {"min": 400, "max": 599, "label": "400-599人", "color": "#FF0000"},
                                     {"min": 599, "max": 9999, "label": "599-9999人", "color": "#8B0000"}
                                 ])      # color

)
my_map.render()
