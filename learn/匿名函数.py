#codng=utf-8
#匿名函数
def edit_story(words,func):
    for word in words:
        print(func(word))

def enliven(word):
    return word.capitalize()+'!'

stairs=['thud','neow','thud','hiss']

# print(edit_story(stairs,enliven))
#
# print(edit_story(stairs,lambda word:word.capitalize()+'!'))
#
# print(list(map(lambda word:word.capitalize()+'!',stairs)))


##############################################################
#生成器
print(sum(range(1,101)))

def my_range(star1,stop1,step1=1):
    number=star1
    while number<stop1:
        yield number
        number+=step1


print(type(my_range(1,5)))

for i in my_range(1,5,2):
    print(i)























