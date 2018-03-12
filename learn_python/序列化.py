#coding=utf-8
# Python中用于序列化的两个模块
#
# json     用于【字符串】和 【python基本数据类型】 间进行转换
# pickle   用于【python特有的类型】 和 【python基本数据类型】间进行转换
# Json模块提供了四个功能：dumps、dump、loads、load
#
# pickle模块提供了四个功能：dumps、dump、loads、load

import json
#json.dumps()将python基本数据类型转化为字符串形式
dic={'k1':'v1'}
print(dic,type(dic)) #现在dic是字典类型

result=json.dumps(dic) #dic 转化为字符串
print(result,type(result))

## json.loads() 将python字符串形式转化成基本数据类型
s='{"k1":123}'
print(s,type(s)) #现在是字符串类型

dic=json.loads(s)  #将字符串转化为基本数据类型，这里转化为dic字典！
print(dic,type(dic))

#json.dump()先序列化，在写入文件
li=[1,2,3,4,5]
json.dump(li,open('dbb','w'))

#json.load()读取文件反序列化
l=json.load(open('dbb','r'))
print(l,type(l))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import pickle
####pickle
#pickple只有python才能用,用于复杂类型的序列化,
#(如果是序列化一个对象,在别的模块中反序列化的时候一定要导入该对象所属的类,否则报错)

#oickle序列化
li=[11,22,33]
r= pickle.dumps(li)
print(r) #返回一个内存对象

result=pickle.loads(r) #使用load反序列化回来
print(result,type(result))

# pickle.dump() 先序列化，再写入文件
ll=[11,22,33]
pickle.dump(ll,open('dbb','wb'))

# pickle.load() 读取文件反序列化
aa=pickle.load(open('dbb','rb'))
print(aa,type(aa))


#####################
#     shutil
#高级的 文件、文件夹、压缩包 处理模块，注意当前用户要是对其他文件或目录没有权限会报错

import shutil

#shutil.copyfileobj(open('aa.txt','r',encoding='utf-8'),open('test','w+',encoding='utf-8'))
#将文件内容拷贝到另一个文件中

shutil.copyfile('aa.txt','aaa.txt')
#复制文件并更换文件名



















