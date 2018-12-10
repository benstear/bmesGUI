#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 17:18:07 2018

@author: dawnstear
"""

import pandas as pd
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
#from plots import ecgplot

ecg = '/Users/dawnstear/desktop/PWC44/ecg.csv'
fnirs = '/Users/dawnstear/desktop/PWC44/PWC44_Oxy.txt'

def ecgplot(filename):
    df = pd.read_csv(filename) 
    clipped_df = df[93184:108000]
    y = clipped_df.values
    return y

y = pd.read_fwf(fnirs)
y.columns = ['1','2','3','4','5','6','7','8','9','10','11',
             '12','13','14','15','16','17','18','19','20']
channel  = y['1'].values
ecgdata = ecgplot(ecg)



# -------------------------------------------
win = pg.GraphicsWindow()
win.setWindowTitle('Scrolling fNIRS data')
chunkSize = 100
maxChunks = 10
startTime = pg.ptime.time()
p5 = win.addPlot(colspan=2)
p5.setLabel('bottom', 'time', 's','oxy concentration')
p5.setXRange(-10, 0)
curves = []
data5 = channel
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

'''
# update all plots
def update():
    update5()
    #update6()'''
'''
# plot ECG data
win.nextRow()
p6 = win.addPlot(colspan=2)
p6.setLabel('bottom', 'Time', 's')
p6.setXRange(-10, 0)
curves = []
data6 = ecgdata#np.empty((chunkSize+1,2))
ptr6 = 0


def update6():
    global p5, data6, ptr6, curves
    now = pg.ptime.time()
    for c in curves:
        c.setPos(-(now-startTime), 0)
    
    i = ptr6 % chunkSize
    if i == 0:
        curve = p6.plot()
        curves.append(curve)
        last = data6[-1]
        data6 = np.empty((chunkSize+1,2))        
        data6[0] = last
        while len(curves) > maxChunks:
            c = curves.pop(0)
            p5.removeItem(c)
    else:
        curve = curves[-1]
    data6[i+1,0] = now - startTime
    data6[i+1,1] = np.random.normal()
    curve.setData(x=data6[:i+2, 0], y=data6[:i+2, 1])
    ptr6 += 1

'''
