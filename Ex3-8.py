'''
@Author: your name
@Date: 2019-11-14 14:40:16
@LastEditTime: 2019-11-14 14:58:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex3-8.py
'''
from scipy import signal
import matplotlib.pyplot
import numpy
import scipy

M = 8
l = numpy.arange(0,2*M+1,1,dtype=int)
print(l)
# 窗函数
wn = numpy.ones([2*M+1])
# 频率范围
omega = numpy.arange(-1*numpy.pi, numpy.pi, 2*numpy.pi/200)
print(omega)
Wd,Hd = signal.freqz(wn,1,omega)
print(Hd)

M1 = 20
l1 = numpy.arange(0,2*M1+1,1,dtype=int)
# 窗函数
wn1 = numpy.ones([2*M1+1])
# 频率范围
Wd1,Hd1 = signal.freqz(wn1,1,omega)

# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 3.7')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(211)
# 使用 plot 函数绘制
matplotlib.pyplot.plot((Wd/numpy.pi),20*numpy.log10(abs(Hd)))
# 标识
matplotlib.pyplot.title("Frequency response")
matplotlib.pyplot.ylabel('Magnitude')
# matplotlib.pyplot.xlabel('Normalized frequency')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(212)
# 使用 plot 函数绘制
matplotlib.pyplot.plot((Wd1/numpy.pi),20*numpy.log10(abs(Hd1)))
# 标识
# matplotlib.pyplot.title("Frequency response")
matplotlib.pyplot.ylabel('Magnitude')
matplotlib.pyplot.xlabel('Normalized frequency') 
# 使用 show 函数显示
matplotlib.pyplot.show()
# EOF
