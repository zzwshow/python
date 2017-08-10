#coding=utf-8

class Instance:
    __instance = None #私有类属性

    def __init__(self):
        self.name='name'
        self.passwd='kkkk'

    @staticmethod   #静态方法，析构函数
    def get_instance():
        if not Instance.__instance:
            Instance.__instance=Instance()

        return Instance.__instance
obj1=Instance.get_instance()
obj2=Instance.get_instance()








