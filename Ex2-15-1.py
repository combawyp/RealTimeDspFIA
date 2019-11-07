'''
@Author: your name
@Date: 2019-11-07 17:05:42
@LastEditTime: 2019-11-07 17:06:00
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex2-15-1.py
'''
from scipy import signal
import matplotlib.pyplot
import numpy

b   = [1,0,0,0,0,0,0,0,-1]
a   = [1, -1.1]
w,h = signal.freqz(b,a)

fig, ax1 = matplotlib.pyplot.subplots()
ax1.set_title('frequency response')
ax1.plot(w/numpy.pi, 20 * numpy.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [pi*rad/sample]')

ax2 = ax1.twinx()
angles = numpy.unwrap(numpy.angle(h))
ax2.plot(w/numpy.pi, 180*angles/numpy.pi, 'g')
ax2.set_ylabel('Angle (degrees)', color='g')
ax2.grid()
ax2.axis('tight')

matplotlib.pyplot.show()
