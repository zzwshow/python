#coding=utf-8
# import time
# def consumer(name):
#     print('%s 开始吃包子了'% name)
#     while True:
#         baozi = yield  #不但能返回值还能接收值
#         print('包子 [%s]来了，被吃了[%s]吃了'%(baozi,name))
#
#
# def producer(name):
#     c = consumer('A')
#     b = consumer('b')
#     c.__next__()     #调用函数执行一步
#     b.__next__()
#     print("要吃包子了")
#     for i in range(10):
#         time.sleep(1)   #休息1秒钟
#         print('做了2个包子')
#         c.send(i)  #发送给上面的yield
#         b.send(i)
#
# producer('zzw')



#########################################
#打开文件yield 一行一行的返回
def gen_data_from_file(file_name):
    for line in open(file_name):
        yield line
        

#接收上面的返回行，并去掉空格   返回单词生成器 需要用for 来读取单词
def gen_words(line):
    for word in (w for w in line.split() if w.strip()):
        yield word


def count_words(file_name): #计算文件中每个单词出现的次数！返回一个字典!
    word_map = {}
    for line in gen_data_from_file(file_name):
        for word in gen_words(line):
            if word not in word_map:
                word_map[word] = 0
            word_map[word] += 1
    return word_map


def count_total_chars(file_name): #计算文件中包含的单词总个数
    total = 0
    for i in gen_data_from_file(file_name):
        total += len(i.strip())
    
    return total


if __name__ == '__main__':
    for ii in gen_data_from_file('test.txt'):
        for i in gen_words(ii):
            print(i)
		
    print(count_words('test.txt'))
    print(count_total_chars('test.txt'))


