'''
@Author: your name
@Date: 2019-11-08 10:06:19
@LastEditTime: 2019-11-08 10:48:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Exp2-16.py
'''
# 正弦波增益 A=1， 频率 f=1000Hz， 采样频率 10000Hz
import numpy
import matplotlib.pyplot

N   = 100
f   = 1000
fs  = 10000
# 使用 arange 函数创建
n   = numpy.arange(0,N-1,1,dtype=int)
print(n)
k   = numpy.arange(0,N-1,1,dtype=int)
print(k)

# 计算正玄波频率 2πf/fs
omega   = 2*numpy.pi*f/fs
print(omega)

# 生成正弦波序列
xn  = numpy.sin(omega*n)
print(xn)

# 对正弦波运算FFT
Xk  = numpy.fft.fft(xn,N-1)
print(Xk)

# 计算幅度谱
magXk   = 20*numpy.log10(abs(Xk))
print(magXk)

# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 2.16')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(111)
# 使用 plot 函数绘制，标注方式 o
matplotlib.pyplot.plot(k,magXk)
# 
matplotlib.pyplot.xlim(0,N/2)
# 使用 show 函数显示
matplotlib.pyplot.show()
# EOF