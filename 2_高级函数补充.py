# zip() 函数
# 把两个可迭代的内容生成一个可迭代的tuple 元素类型组成的内容
#
#l1 = ["王明", "明悦", "秋水"]
#l2 = [89, 22, 11]
#z = zip(l1, l2)
#for item in z:
#    print(item)

# 考虑列表生成式

# ------------------------------------------
# enumerate()
# 与 zip() 功能相像
# 对可迭代对象里的每一个元素，配上一个索引，然后索引和内容的构成　tuple　类型
#
#l1 = [1, 2, 3, 4, 5]
#result = enumerate(l1)
#l2 = [i for i in result]
#print(l2)

# ------------------------------------------

#collections 模块
# namedtuple
# 可命名的tuple
import collections

Circle = collections.namedtuple('Circle', ['x', 'y', 'r'])
c1 = Circle(1, 2, 3)
print(c1)



# ------------------------------------------
# deque
#from collections import deque
#q = deque(['a', 'b', 'c'])
#q.appendleft('x')
#print(q)
#q.popleft()
#print(q)
# ------------------------------------------

# defaultdict
# 当直接读取  dict 不存在的　ｋｅｙ　时，直接返回默认值

#from collections import defaultdict
#
#func = lambda: '666'
#d2 = defaultdict(func)
#
#d2['one'] = 1
#d2['two'] = 2
#print(d2['one'])
#print(d2['rne'])
# ------------------------------------------

# Counter 统计字符串个数
from collections import Counter

list1 = ['liudana', 'niubi', 'niubi', 'dana', '666', '666']
s = Counter(list1)
print(s)
# ------------------------------------------




