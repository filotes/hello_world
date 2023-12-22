"""
list(容器)
将给定的容器转换为列表

str(容器)
将给定的容器转换为字符串

tuple(容器)
将给定的容器转换为元组

set(容器)
将给定的容器转换为集合
"""

# 容器的排序
# 正向排序(从小到大)sorted(容器)
# 反向排序(从小到大)sorted(容器， reverse=True)
# 排序后变成列表对象


# 排序
# sorted(序列)    正向排序(从大到小)
# sorted(序列, reverse=True)    反向排序(从小到大)
# 字符串的比较    ASCII码表
li = {1, 2, 3, 4, 5}
print(max(li))
gi = {"a", "b", "c", "d", "e", "A", "B", "C", "D", "E"}
print(max(gi))
print(sorted(li))
print(sorted(li, reverse=True))
print(sorted(gi))
print(sorted(gi, reverse=True))

# 字符串是安位比较，也就是一位一位进行对比，只要有一位大，那么整体就大

s1 = "abcde"
s2 = "ABCDE"

print(f"{s1}大于{s2}的结果: {s1 > s2}")
print(f"{s2}大于{s1}的结果: {s2 > s1}")
print(f"key2 > key1, 结果: {"key2" > "key1"}")