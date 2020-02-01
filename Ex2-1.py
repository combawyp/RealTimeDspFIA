'''
@Author: your name
@Date: 2019-11-07 10:15:00
@LastEditTime: 2019-11-07 11:12:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex2-1.py
'''
import numpy
import matplotlib.pyplot
 
# 方法 0： 复杂不建议使用
# 使用 range 函数创建列表对象  
# 使用 iter 函数创建迭代器 
# 使用迭代器创建 ndarray 
# n       = numpy.fromiter(iter(range(0,31)),dtype=int)
# 方法 1：
# 使用 arange 函数创建
n       = numpy.arange(0,31,1,dtype=int)
print(n)

omega   = 0.25*numpy.pi
print(omega)

xn      = 2*numpy.sin(omega*n)
print(xn)

# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 2.1')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(111)
# 使用 plot 函数绘制，标注方式 o
matplotlib.pyplot.plot(n,xn,'-o')
# 使用 show 函数显示
matplotlib.pyplot.show()
# EOF