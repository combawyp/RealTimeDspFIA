'''
@Author: your name
@Date: 2019-11-08 14:00:44
@LastEditTime: 2019-11-08 14:07:22
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex2-21.py
'''
import numpy
import matplotlib.pyplot

N   = 256
# 生成序列 0到255
n   = numpy.arange(0, N-1, 1, dtype=int)
print(n)

# 生成具有单位方差的随机数列
delta  = numpy.sqrt(3)
vn  = numpy.random.uniform(-1*delta, delta, size=N-1)
print(vn)

# 生成正弦波数列
# 计算正玄波频率 2πf/fs
omega   = 0.2*numpy.pi
print(omega)

# 生成正弦波序列
sn  = numpy.sin(omega*n)
print(sn)

xn=sn+vn

# 对正弦波运算FFT
Xk  = numpy.fft.fft(xn,N-1)
print(Xk)
# 计算dB值
magX    = 20*numpy.log10(abs(Xk))

# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 2.20')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(111)
# 使用 plot 函数绘制
matplotlib.pyplot.plot(n,magX)
# 显示一半
matplotlib.pyplot.xlim(0,N/2)
# 使用 show 函数显示
matplotlib.pyplot.show()
# EOF