# 定义一个字典
# key: value    key不可为字典
my_dict = {"王力宏": 88, "周杰伦": 92, "林俊杰": 92}

# 定义空字典
dict1 = {}
dict2 = dict()

# 字典数据的获取
print(my_dict["王力宏"])
print(my_dict["周杰伦"])
print(my_dict["林俊杰"])

my_dict1 = {
    "王力宏":
        {"语文": 77, "数学": 66, "英语": 33, "爱好": "唱，跳，rap,篮球"},
    "周杰伦":
        {"语文": 77, "数学": 86, "英语": 55},
    "林俊杰":
        {"语文": 99, "数学": 96, "英语": 66}
}
yw = my_dict1["王力宏"]["语文"]
sx = my_dict1["王力宏"]["数学"]
yy = my_dict1["王力宏"]["英语"]
ah = my_dict1["王力宏"]["爱好"]
print(f"王力宏的语文成绩是{yw}")
print(f"王力宏的数学成绩是{sx}")
print(f"王力宏的英语成绩是{yy}")
print(f"王力宏的爱好是{ah}")

my_dict2 = {
    "周杰伦": 88,
    "王力宏": 77,
    "凌俊杰": 99
}
# 字典的新增元素
# 语法：   字典[key] = Value，    结果：字典被修改，新增了元素
my_dict2["张学友"] = 66
print(my_dict2)

# 更新元素
# 语法：   字典[key] = Value，    结果：字典被修改，元素被更新
# 注意：   字典key不可重复，所以对已存在key执行上述操作，就是更行Value值
my_dict2["王力宏"] = 100
print(my_dict2)
my_dict2["蔡徐坤"] = 11
print(my_dict2)

# 删除元素
# 语法:   字典.pop(Key)
# 结果    获得指定Key的Value,同时字典被修改,指定Key的数据被删除

my_dict2 = {
    "周杰伦": 88,
    "王力宏": 77,
    "凌俊杰": 99
}
pop1 = my_dict2.pop("王力宏")
print(pop1)
print(my_dict2)

# 清空字典
# 语法:   字典.clear()  结果:字典被修改,元素被清空

my_dict2 = {
    "周杰伦": 88,
    "王力宏": 77,
    "凌俊杰": 99
}
my_dict2.clear()
print(my_dict2)

# 获取全部Key
# 语法:   字典.Keys()
# 结果:       得到字典中的全部Key

my_dict2 = {"周杰伦": 88, "王力宏": 77, "凌俊杰": 99}
key = my_dict2.keys()
print(key)
# 遍历字典
for x in key:
    print(f"字典的Key是{x}")
    print(f"字典的Value是{my_dict2[x]}")

# 方式
for n in my_dict2:
    print(f"字典的Key是{n}")

# 统计字典的元素数量
g = len(my_dict2)
print(g)

my_dictv = {
    "蔡徐坤": {
        "部门": "科技部",
        "工资": 1145,   "级别": 1},
    "吴亦凡": {
        "部门": "市场部",
        "工资": 1146,
        "级别": 1},
    "周杰伦": {
        "部门": "技术部",
        "工资": 1147,
        "级别": 4},
    "李易峰": {
        "部门": "牛马部",
        "工资": 1148,
        "级别": 5},
    "马超": {
        "部门": "ikun部",
        "工资": 1149,
        "级别": 1}
}
for xx in my_dictv:
    b = my_dictv[xx]
    # print(b)
    # print(type(b))
    # c = b["级别"]
    if b["级别"] == 1:
        b["级别"] += 1
        # gg = b["工资"]
        # gg = int(gg)
        # gg += 1000
        # b["工资"] = gg
        b["工资"] += 1000
print(f"全体级别为1的加1,工资加1000后为{my_dictv}")

