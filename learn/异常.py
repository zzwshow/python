#coding=utf-8

#异常

short_list=[1,2,3,4,5]

position=4

try:
	print(short_list[position])  #要执行的代码块
	
except: #捕捉到异常执行下面的代码！
	print('Need a position between 0 and',len(short_list)-1 ,',but got position.')

########################################

short_list=[1,2,3]

while True:
	value=input('Please input a number!["q" and "quite" is break!]:')
	if value == 'q' or value == 'quite':
		break
	try:
		position = int(value)
		print(short_list[position])
	except IndexError as e:     #捕捉指定异常！
		print('Bad Index:',e)

	except Exception as error:   #捕捉其他异常！
		print('Something else broke:',error)
		
######################################
#编写自己的异常！
class UppercaseException(Exception):
	pass

words=['eeenie','meenie','miny','MO']
for word in words:
	if word.isupper():
		raise UppercaseException(word)














