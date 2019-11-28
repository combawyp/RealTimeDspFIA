'''
@Author: your name
@Date: 2019-11-14 16:17:57
@LastEditTime: 2019-11-28 15:04:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex3-9.py
'''
from scipy import signal
import matplotlib.pyplot
import numpy
import scipy

omegac = 0.4*numpy.pi   # 截止频率
L = 61                  # 滤波器长度
M = (L-1)/2
l = numpy.arange(0,2*M+1,1,dtype=int)
# 计算冲激响应
h = omegac/numpy.pi*scipy.sinc(omegac*(l-M)/numpy.pi) 
#  海明窗
wn = numpy.hamming(L)
# 新的传递函数
hwn = h*wn
print(hwn)
# 原始滤波器频率范围
omega = numpy.arange(-1*numpy.pi, numpy.pi, 2*numpy.pi/200)
Wd,Hd = signal.freqz(h,1,omega)

# 增加海明窗滤波器频率范围
Whd,Hhd = signal.freqz(hwn,1,omega)

fig, ax1 = matplotlib.pyplot.subplots()
ax1.set_title('Hamming')
ax1.plot(Wd/numpy.pi, abs(Hd), 'y')
ax1.plot(Whd/numpy.pi, abs(Hhd), 'g')
ax1.set_ylabel('Amplitude', color='b')
ax1.set_xlabel('Frequency [pi*rad]')

# 画网格
ax1.grid()
ax1.axis('tight')
# 使用 show 函数显示
matplotlib.pyplot.show()
# EOF