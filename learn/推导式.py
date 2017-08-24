#coding=utf-8

#列表推导式
print([ i for i in range(10) if i % 2 !=1])
#字典推导式！
word='letters'
letter_counts={letter:word.count(letter) for letter in word}
print(letter_counts)

#集合推导式
a_set={number for number in range(1,6) if number % 3 ==1}
print(a_set)
 
#生成器推导式
number_thing=(number for number in range(1,6))
print(type(number_thing))


#使用字典推导式，把（0，9）的整数作为建，平方作为值
squares ={num:num*num for num in range(9)}
print(squares)

