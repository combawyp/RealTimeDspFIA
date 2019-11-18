'''
@Author: your name
@Date: 2019-11-14 11:33:42
@LastEditTime: 2019-11-14 14:40:55
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex3-7.py
'''
from scipy import signal
import matplotlib.pyplot
import numpy
import scipy

omegac = 0.4*numpy.pi   # 截止频率
L = 61                  # 滤波器长度
M = (L-1)/2
l = numpy.arange(0,2*M+1,1,dtype=int)
print(l)
# 计算冲激响应
h = omegac/numpy.pi*scipy.sinc(omegac*(l-M)/numpy.pi) 
print(h)
# 频率范围
omega = numpy.arange(-1*numpy.pi, numpy.pi, 2*numpy.pi/200)
print(omega)
Wd,Hd = signal.freqz(h,1,omega)
print(Hd)

# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 3.7')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(111)
# 使用 plot 函数绘制
matplotlib.pyplot.plot((Wd/numpy.pi),abs(Hd))
# 标识
matplotlib.pyplot.title("Frequency response")
matplotlib.pyplot.ylabel('Magnitude')
matplotlib.pyplot.xlabel('Normalized frequency')
# 使用 show 函数显示
matplotlib.pyplot.show()
# EOF