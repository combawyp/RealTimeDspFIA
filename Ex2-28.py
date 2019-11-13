'''
@Author: your name
@Date: 2019-11-13 10:47:04
@LastEditTime: 2019-11-13 15:33:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex2-28.py
'''
# 暂时没有找到合适量化器，没有合适 python 实现
# 考虑要不要自己写一个 :(
import numpy
import matplotlib.pyplot

N = 16
Q = 32
# 生成随机序列 0~N-1
n = numpy.arange(0,N,1,dtype=int)
# 生成零均值白噪音
delta = numpy.sqrt(3)
xn = numpy.random.uniform(-1*delta, delta, size=N)

# 格式量化
Qa = 15
XQa = (xn * (2**Qa)).astype(int)
print(XQa)

# 格式量化
Qb = 3
XQb = (xn * (2**Qb)).astype(int)*(2**(Qa-Qb))
print(XQb)

# 计算误差
en = XQa - XQb
print(en)

# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 2.28')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(111)
# 使用 plot 函数绘制
matplotlib.pyplot.plot(n,en)
matplotlib.pyplot.plot(n,XQa,'-x')
matplotlib.pyplot.plot(n,XQb,'-o')
# 使用 show 函数显示
matplotlib.pyplot.show()
# EOF