'''
@Author: your name
@Date: 2019-12-05 08:58:28
@LastEditTime: 2019-12-05 09:07:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex4-16.py
'''
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
# print(xn)

# 生成正弦波数列
# 计算正玄波频率 2πf/fs
omega   = 0.6*numpy.pi
# print(omega)

# 生成正弦波序列
sn  = numpy.sin(omega*n)
# print(sn)

# 生成正弦波数列
# 计算正玄波频率 2πf/fs
omegaB   = 0.9*numpy.pi
# print(omega)

# 生成正弦波序列
snB  = numpy.sin(omegaB*n)
# print(sn)

# 生成正弦波数列
# 计算正玄波频率 2πf/fs
omegaC   = 0.2*numpy.pi
# print(omega)

# 生成正弦波序列
snC  = numpy.sin(omegaC*n)
# print(sn)


xn  = xn+3*sn+3*snB+3*snC
#xn = sn
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
# print(Nn)
# print(Wn)
# IIR滤波器
b,a = scipy.signal.butter(Nn, Wn, btype='bandpass',analog=True)
# print(a)
# print(b)
# 将直接型滤波器转换成二阶级联结构
sos = scipy.signal.tf2sos(b,a)
# print(sos)
# 滤波
y   = scipy.signal.sosfilt(sos,xn)
print(y)

# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 4.16')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(211)
# 使用 plot 函数绘制白噪音
matplotlib.pyplot.plot(n,xn)
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(212)
# 使用 plot 函数绘制输出
matplotlib.pyplot.plot(n,y)
# 使用 show 函数显示
matplotlib.pyplot.show()

Xk = numpy.fft.fft(xn,N-1)
Yk = numpy.fft.fft(y,N-1)
# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 4.16 频谱')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(211)
# 使用 plot 函数绘制白噪音
matplotlib.pyplot.plot(n,abs(Xk))
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(212)
# 使用 plot 函数绘制输出
matplotlib.pyplot.plot(n,abs(Yk))
# 使用 show 函数显示
matplotlib.pyplot.show()

# EOF