

def te(name):
    return name[1]


b = [["稻妻", 5], ["璃月", 1], ["蒙德", 2], ["须弥", 3], ["枫丹", 4]]

b.sort(key=te)
print(b)


b.sort(key=lambda g: g[1], reverse=True)
print(b)
