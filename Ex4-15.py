'''
@Author: your name
@Date: 2019-11-28 15:40:29
@LastEditTime: 2019-11-28 17:01:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex4-15.py
'''
# 程序还有问题，感觉滤波的效果完全看不出来

from scipy import signal
import matplotlib.pyplot
import numpy
import scipy

N   = 400
Fs  = 1000

# 生成序列 0到300
n   = numpy.arange(0, N-1, 1, dtype=int)
# print(n)
# 生成具有单位方差的随机数列
delta  = numpy.sqrt(3)
xn  = numpy.random.uniform(-1*delta, delta, size=N-1)

# 生成正弦波数列
# 计算正玄波频率 2πf/fs
omega   = 0.8*numpy.pi

# 生成正弦波序列
sn  = numpy.sin(omega*n)

xn  = xn+30*sn
# xn = sn
# 通带边沿频率,浮点序列
Wp  = numpy.array([140, 160],dtype=float)/(Fs/2)
# 阻带边沿频率,浮点序列
Ws  = numpy.array([130, 170],dtype=float)/(Fs/2)
# 通带纹波
Rp  = 3
# 阻带纹波
Rs  = 40
# 计算滤波器阶数
Nn,Wn = scipy.signal.buttord(Wp, Ws, Rp, Rs)
# IIR滤波器
b,a = scipy.signal.butter(Nn, Wn, btype='band',analog=True)
# 对白噪音进行滤波
y   = scipy.signal.lfilter(b, a, xn)

# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 4.15 时域信号')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(221)
# 使用 plot 函数绘制白噪音
matplotlib.pyplot.plot(n,xn)
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(222)
# 使用 plot 函数绘制输出
matplotlib.pyplot.plot(n,y)

Xk = numpy.fft.fft(xn)
Yk = numpy.fft.fft(y)
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(223)
# 使用 plot 函数绘制白噪音
matplotlib.pyplot.plot(n,20*numpy.log10(abs(Xk)))
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(224)
# 使用 plot 函数绘制输出
matplotlib.pyplot.plot(n,20*numpy.log10(abs(Yk)))
# 使用 show 函数显示
matplotlib.pyplot.show()

# EOF