'''
@Author: your name
@Date: 2019-12-11 11:20:20
@LastEditTime: 2019-12-11 14:52:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex5-10.py
'''
from scipy import signal
import matplotlib.pyplot
import numpy
import scipy

f   = 100    # 信号频率
f_s = 256   # 采样频率

N   = 128   # 信号点数
n   = numpy.arange(0, N, 1, dtype=int)    # 生成序列 0 ~ N-1
x_n = numpy.sin(n*2*scipy.pi*f/f_s)       # 生成正弦序列

N_fft   = 512 # FFT 点数
n_fft   = numpy.arange(0, N_fft, 1, dtype=int)

# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 5.10 正弦波时域')
# 使用 plot 函数绘制时域信号
matplotlib.pyplot.plot(n,x_n)
# 使用 show 函数显示
matplotlib.pyplot.show()

X_k = scipy.fft(x_n, N_fft)    # 对信号进行N点fft
F_k =  n_fft*f_s/N_fft         # 计算每点对应的频率
# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 5.10 正弦波频域')
# 使用 plot 函数绘制时域信号
matplotlib.pyplot.plot(F_k,abs(X_k))
# 设置x轴范围
matplotlib.pyplot.xlim(0,f_s/2)
matplotlib.pyplot.xlabel("Hz")
# 使用 show 函数显示
matplotlib.pyplot.show()

# EOF