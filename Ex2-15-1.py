'''
@Author: your name
@Date: 2019-11-07 17:05:42
@LastEditTime: 2019-11-08 10:06:29
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex2-15-1.py
'''
# 显示的跟 matlab 并不一致，角度偏移不一致
# 而且当参数 a[1,-1] 时运算出错，怀疑是一个不稳定的系统参数
from scipy import signal
import matplotlib.pyplot
import numpy

b   = [1,0,0,0,0,0,0,0,-1]
a   = [1, -0.9]
w,h = signal.freqz(b,a)

fig, ax1 = matplotlib.pyplot.subplots()
ax1.set_title('frequency response')
ax1.plot(w/numpy.pi, 20 * numpy.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [pi*rad/sample]')

ax2 = ax1.twinx()
angles = numpy.unwrap(numpy.angle(h))
ax2.plot(w/numpy.pi,(180*(angles/numpy.pi)), 'g')
ax2.set_ylabel('Angle (degrees)', color='g')
ax2.grid()
ax2.axis('tight')

matplotlib.pyplot.show()
