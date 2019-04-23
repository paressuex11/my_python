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
# logging.exception(e)打印错误栈
#def drawCircleTurtle(x, y, r):
#    tur.up()
#    tur.setpos(x + r, y)
#    tur.down()

#    for i in range(0, 365, 5):
#        a = math.radians(i)
#        tur.setpos(x + r*math.cos(a), y + r*math.sin(a))
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


#class Matrix:
#    def __init__(self, *args, **kwargs):
#        return super().__init__(*args, **kwargs)

#ma = Matrix()

#print(ma.__hash__());
#ma.rows = 1;
#def foo(s):
#    return 10 / int(s)

#def bar(s):
#    return foo(s) * 2

#def main():
#    bar('0')

#main()
#import threading
#def a():
#    aa = 1
#while 1:
#    th = threading.Thread(target = a)
#    th.start()
#    th.join()
import numpy as np
import matplotlib.pyplot as pyplot
def main():
    """
    绘制方波
    """
    #x = np.linspace(-np.pi, np.pi, 200)
    #k = np.arange(1, 200)
    #miu = 2 * k - 1
    #f = np.zeros_like(x)
    #for i in range(len(x)):
    #    f[i] = np.sum(np.sin(miu * x[i]) * miu)
    #f = f * 4 / np.pi
    #pyplot.plot(x, f)
    #pyplot.show()
    #绘制失败


    M = np.mat("1 2 3; 4 5 6 ; 7 8 9")
    print(M[...,:2])
    nn = np.linalg.pinv(M)
    print(np.linalg.eig(M))
    print(nn.dot(M))

#numpy learning 
#linspace()生成一个组均匀分布的数据
#array[:,1]获取一列
#ndarray[...,1]
#array.compress筛选数据
#array.flat数组迭代器
#array.flatten()把数组铺平
#array.resize()原地修改数组的size, array.reshape()生成新数组
#split(array, number, axis = ?) 数组分割
#concatenate((arr1, arr2), axis = ?)数组合并
#column_stack((arr1, arr2)) 两个一维数组当成列向量后合并
#array的广播甚至允许bool运算，只不过array会变成bool type 
#np.extract(bool_array, array2) 从array2里抽取元素
 

#numpy.linalg
#mat("1 1 1; 1 1 1; 2 2 2;")
#np.linalg.solve(mat, array) 求解Ax = b
#linalg.eigvals(mat) 求特征值
#linalg.eig(mat) 返回一个(array for eigenvalues, matrix for eigenvectors)matrix好像是列向量来的
#np.dot 点乘
#linalg.svd(mat) 奇异值分解， 返回左矩阵， 奇异值列表(中间矩阵的值)，右矩阵

#matplotlib
#subplot(int) int一般由三位数字组成 行数 列数 序号(从1开始)
#hist()直方图
#bar()条形图

#pandas
#read_excel(filepath) 读取filepath的文件返回一个dataframe(推荐预装xlwt和xlrd)
#dataframe.rename(columns = dict, axis) dict的键是原来的列索引，值是新的列索引
#Series.value_count() 返回一个series是值和出现次数series
#dataframe.columns 返回列索引列表
#dataframe.values 把每一行当成一项返回它们的集合
#dataframe[index] 返回列索引为index的列
#dataframe[boolean expressions] 可以筛选dataframe内容
    #例如： dataframe[dataframe[index] >= 90] 可以返回dataframe 的第index列(index不一定是int)的值>=90的项们
    #dataframe[index1, index2][(dataframe[index] >= 90) & (dataframe[index] <= 100)] 多个筛选条件可以括号后用bool表达式写出来，前面那个中括号是仅显示哪些列
#series.sort_index() 按索引排序 series.sort_values() 按值排序



if __name__ == "__main__":
    main()