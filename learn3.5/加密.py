#coding=utf-8
import hashlib
hash1=hashlib.md5()

hash1.update(bytes('admin',encoding='utf-8'))
print(hash1.hexdigest())

print(hash1.digest())

#以上加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。
# 所以，有必要对加密算法中添加自定义key再来做加密。　

hash=hashlib.md5(bytes('898abc090',encoding='utf-8'))
hash.update(bytes('admin',encoding='utf-8'))
print(hash.hexdigest())

if 'cf1a70b67d70f426c86c9d8338687871' == hash.hexdigest():
    print('OK')
else:
    print('error')





