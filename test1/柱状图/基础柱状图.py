from pyecharts.charts import Bar
from pyecharts.options import *

bar = Bar()

bar.add_xaxis(["中国", "美国", "英国"])

bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"), color="red")  # 数字显示到右边

# 反转x和y轴
bar.reversal_axis()

bar.set_global_opts(
    visualmap_opts=VisualMapOpts(is_show=True, is_piecewise=True, pieces=[
        {"min": 1, "max": 10, "label": "1-10人", "color": "#00868B"},
        {"min": 11, "max": 20, "label": "11-20人", "color": "#FFFF00"},
        {"min": 21, "max": 30, "label": "21-30人", "color": "#90EE90"},

    ])

)
bar.render("柱状图.html")
