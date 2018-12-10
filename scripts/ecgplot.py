#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 08:48:17 2018

@author: dawnstear
"""

import pandas as pd
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

ecg = '/Users/dawnstear/desktop/PWC44/ecg.csv'

def ecgplot(filename):
    df = pd.read_csv(filename) 
    clipped_df = df[1000000:1200000]
    y = clipped_df.values
    return y

ecgdata = ecgplot(ecg)

win = pg.GraphicsWindow()
win.setWindowTitle('Scrolling heart rate (ECG) data')
chunkSize = 100
maxChunks = 10
startTime = pg.ptime.time()
p5 = win.addPlot(colspan=2)
p5.setLabel('bottom', 'time', 's','voltage')
p5.setXRange(-10, 0)
#p5.setYRange(1800,2700)
curves = []
data5 = ecgdata
ptr5 = 0

def update5():
    global p5, data5, ptr5, curves
    now = pg.ptime.time()
    for c in curves:
        c.setPos(-(now-startTime), 0)
    
    i = ptr5 % chunkSize
    if i == 0:
        curve = p5.plot()
        curves.append(curve)
        last = data5[-1]
        data5 = np.empty((chunkSize+1,2))        
        data5[0] = last
        while len(curves) > maxChunks:
            c = curves.pop(0)
            p5.removeItem(c)
    else:
        curve = curves[-1]
    data5[i+1,0] = now - startTime
    data5[i+1,1] = np.random.normal()
    curve.setData(x=data5[:i+2, 0], y=data5[:i+2, 1])
    ptr5 += 1
    

    
timer = pg.QtCore.QTimer()
timer.timeout.connect(update5)
timer.start(50)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()



