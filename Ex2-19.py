'''
@Author: your name
@Date: 2019-11-08 11:24:08
@LastEditTime: 2019-11-08 11:48:41
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex2-19.py
'''
import numpy
import matplotlib.pyplot

N   = 256
# 生成序列 0到255
n   = numpy.arange(0, N-1, 1, dtype=int)
print(n)

# 生成具有单位方差的随机数列
delta  = numpy.sqrt(3)
xn  = numpy.random.uniform(-1*delta, delta, size=N-1)
print(xn)

# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 2.19')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(111)
# 使用 plot 函数绘制
matplotlib.pyplot.plot(n,xn)
# 使用 show 函数显示
matplotlib.pyplot.show()
# EOF