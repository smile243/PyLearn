def myFunction():
    print('The value of __name__ is ' + __name__)


"""
需要让某些代码只在该模块作为主程序运行时才执行，而不是被其他模块 import 引入时就执行。
这时候可以使用 if __name__ == '__main__' 这个条件语句
"""
if __name__ == '__main__':
    myFunction()
