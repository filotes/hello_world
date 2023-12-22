"""
什么是json
json是一种轻量级的数据交互格式，可以按照json指定的格式去组织和封装数据
json本质上是一个带有特定格式的"字符串"

主要功能：   json就是一种在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递的交互，类似于：
国际通用语言——英语
中国56个民族不通地区的通用语言——普通话

json的数据格式可以是
字典
{"name":"admin"."age":18}
也可以是
列表内嵌套字典
[{"name":"admin","age":18},{"name":"root","age":16},{"name":"cis","age":14}]

"""

"""
python数据和json数据的相互转化
导入json模块
"""

import json

# 将python文件转换成json
data1 = {"name": "张三", "age": 18, "zy": "搬砖", "dz": "江西"}
data2 = [{"name": "admin", "age": 18}, {"name": "root", "age": 16}, {"name": "cis", "age": 14}]
data3 = json.dumps(data1, ensure_ascii=False)  # 中文想要显示应输入ensure_ascii=False
print(type(data3))
print(data3)
data4 = json.dumps(data2)
print(type(data4))
print(data4)

# 将json转换为python文件
a = '{"name": "张三", "age": 18, "zy": "搬砖", "dz": "江西"}'
b = '[{"name": "admin", "age": 18}, {"name": "root", "age": 16}, {"name": "cis", "age": 14}]'
aa = json.loads(a)
print(type(aa))
print(aa)

bb = json.loads(b)
print(type(bb))
print(bb)

# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
line.add_yaxis("GDP", [30, 20, 10])

# 设置全局配置项set_global_opts
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),        # 控制标题内容和位置
    legend_opts=LegendOpts(is_show=True),       # 控制图列
    toolbox_opts=ToolboxOpts(is_show=True),     # 控制工具箱是否显示
    visualmap_opts=VisualMapOpts(is_show=True)      # 视觉映射
)
# 生成图表
line.render()
