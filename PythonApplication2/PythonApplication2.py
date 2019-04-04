import math
import turtle 
#tur = turtle.Turtle()
# python里不存在块级作用域，但存在局部作用域eg:functions
#python 的类"鸭子类型" ：一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
    #多态的强大之处
#@property装饰器可以把方法变成属性调用
#由于Python允许使用多重继承，因此，MixIn就是一种常见的设计
#__repr__()返回调试用信息，比如在解释器里直接输入一个对象
#__str__()返回用户看到的字符串,也就是print函数调用的方法
#可loop对象要实现__iter__() 和 __next__()
    #__iter__()一般返回自己 ， __next__() 返回loop要返回的下一个东西
    #__getitem__() 方法是返回索引运算符的值, 此方法的参数可以是切片， 用isinstance 来判断; __setitem__()重载索引赋值
#python 生成类的本质是调用type函数，自建metaclass的时候应继承type类

#except可以捕获一个异常以及它的子类异常
def drawCircleTurtle(x, y, r):
    tur.up()
    tur.setpos(x + r, y)
    tur.down()

    for i in range(0, 365, 5):
        a = math.radians(i)
        tur.setpos(x + r*math.cos(a), y + r*math.sin(a))
#drawCircleTurtle(100, 100, 50)
#turtle.mainloop()

#a = []
#def change():
#    a = []
#    print(id(a))
#    return a
#    #print(id(a))
#print(id(a))
#a = change()
#print(id(a))
#f1 = count()
#f2 = f1()
#f3 = f1()
#f4 = f1()
#print(f1,f2,f3,f4)


class Matrix:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

ma = Matrix()

print(ma.__hash__());
ma.rows = 1;


