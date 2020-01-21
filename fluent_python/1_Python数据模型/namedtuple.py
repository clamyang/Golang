from collections import namedtuple
# 创建一个具名元组需要两个参数
# 一个是类名，另一个是类的各个字段的名字。
City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
tokyo = City('Tokyo', 'Jp', 36.933, (35.689722, 139.691667))
print(tokyo)
