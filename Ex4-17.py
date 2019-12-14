'''
@Author: your name
@Date: 2019-12-05 09:16:14
@LastEditTime: 2019-12-05 09:44:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex4-17.py
'''
from scipy import signal
import matplotlib.pyplot
import numpy
import scipy

Fs = 10000              # 采样率 10KHz
# 滤波器1
Wo = 1000/(Fs/2)        # 峰值频率 1KHz
BW = 500/(Fs/2)         # 带宽 500Hz
b,a = scipy.signal.iirpeak(Wo, BW)  # 设计滤波器
# print(a)
# print(b)
# 滤波器2
Wo2 = 2500/(Fs/2)        # 峰值频率 2.5KHz
BW2 = 200/(Fs/2)         # 带宽 200Hz
b2,a2 = scipy.signal.iirnotch(Wo2, BW2)  # 设计陷波器
# 显示滤波器特性
w,h = signal.freqz(b,a)     # 滤波器1特性
w2,h2 = signal.freqz(b2,a2) # 滤波器2特性

# 绘制滤波器特性图
fig, ax1 = matplotlib.pyplot.subplots()
ax1.set_title('frequency response')
ax1.plot(w/numpy.pi, 20 * numpy.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [pi*rad/sample]')

ax2 = ax1.twinx()
ax2.plot(w2/numpy.pi, 20*numpy.log10(abs(h2)), 'g')
ax2.grid()
ax2.axis('tight')

matplotlib.pyplot.show()
# EOF