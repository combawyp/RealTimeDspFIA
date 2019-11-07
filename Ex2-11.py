'''
@Author: your name
@Date: 2019-11-07 14:28:00
@LastEditTime: 2019-11-07 15:27:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \RealTimeDspFIA\Ex2-11.py
'''
from plot_zplane import zplane 

b   = [1]
a   = [1, -1, 0.9]

zplane(b,a)

b   = [1,0,0,0,0,0,0,0,-1]
a   = [1, -1]

zplane(b,a)

# EOF