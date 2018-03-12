#coding=utf-8
#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

from io import StringIO
#很多时候，数据读写不一定是文件，也可以在内存中读写。
f= StringIO() # 创建一个内存对象 f
f.write('HELLO') # 写入字符串
f.write(' ')      #空格
f.write('world')

print(f.getvalue()) #获取 内存对象f中的内容！

#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f= StringIO('hello \n zzw \n goodbye')

for i in f.readlines():
    print(i.strip())

# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())


##################################
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
# print(f.getvalue())

s=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(s.read())












