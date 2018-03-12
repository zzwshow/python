#depue
#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
from collections import deque,defaultdict


q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

print("---------------defaultdict")
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict

dd=defaultdict(lambda :'N/A')
dd['key1']='abc'
print(dd['key1']) # key1存在
print(dd['key2']) # key2不存在，返回默认值



