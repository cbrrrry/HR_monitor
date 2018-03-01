# -*- coding: utf-8 -*-
"""

"""

import serial
import serial.tools.list_ports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, time, math

PORT = 'COM10'
xsize=100

try:
    ser.close();
except:
    print();
    
try:
    ser = serial.Serial(PORT, 115200, timeout=100)
except:
    print ('Serial port %s is not available' % PORT);
    portlist=list(serial.tools.list_ports.comports())
    print('Trying with port %s' % portlist[0][0]);
    ser = serial.Serial(portlist[0][0], 115200, timeout=100)
    ser.isOpen()
#while 1 :
  #  strin = ser.readline();
   # print(strin.decode('ascii'));
    
def data_gen():
    t = data_gen.t
    while True:
       t+=1
       strin = ser.readline();
       y= float (strin);
      # y = strin.decode('ascii');
       yield t, y

def run(data):
    # update the data
    t,y = data
    if t>-1:
        xdata.append(t)
        ydata.append(y)
        if t>xsize: # Scroll to the left.
            ax.set_xlim(t-xsize, t)
        line.set_data(xdata, ydata)
    return line,

def on_close_figure(event):
    sys.exit(0)

data_gen.t = -1
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close_figure)
ax = fig.add_subplot(111)
line, = ax.plot([], [], lw=2)
ax.set_ylim(-5, 200)
ax.set_xlim(0, xsize)
ax.grid()
xdata, ydata = [], []

# Important: Although blit=True makes graphing faster, we need blit=False to prevent
# spurious lines to appear when resizing the stripchart.
ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=100, repeat=False)
plt.show()
