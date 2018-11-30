#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:32:44 2018

@author: dawnstear
"""

import numpy as np
import pandas as pd
from utils import Data
from dimred import DimensionReduction
'''
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore

pg.setConfigOption('leftButtonPan', False)   # set for mac users only,,, put in __main__?
## Switch to using white background and black foreground
pg.setConfigOption('background', 'w')
#pg.setConfigOption('foreground', 'k')
'''


'''  find out how button/lists work to do drop down choiceof dim/red and make that plot it'''
win1=1
win2=0
win3=0

data1k = pd.read_csv('/Users/dawnstear/desktop/Mid_Atlantic_Poster/sc_data/n_1078/data.csv')  
print(np.shape(data1k))

celltypes = data1k['TYPE'] # save cell type vector in case we need it later
labels = data1k['Labels'] # save labels
data_ = data1k.drop(['Labels','TYPE'],axis=1) 
cellcount, genecount = np.shape(data_)
X = data_
y = labels

Utils = Data(X,y)
dr = DimensionReduction(X,y,dataset='1,078')

#pca_data = dr.pca(n_components=2)
lle_data = dr.lle()



'''
# Overhead code
app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.resize(800,800)

view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
mw.setCentralWidget(view)
mw.show()
mw.setWindowTitle('Single-Cell RNA-seq scatter plot')
n = 50

## Make all plots clickable
lastClicked = []
def clicked(plot, points):
    global lastClicked
    for p in lastClicked:
        p.resetPen()
    print("clicked points", points)
    for p in points:
        p.setPen('b', width=2)
    lastClicked = points


if win1:
    # Add plot to GraphicsLayoutWidget
    w1 = view.addPlot()
    # Add Scatter plot to GraphicsLayoutWidget
    s1 = pg.ScatterPlotItem(size=20, pen=pg.mkPen(None),
                            brush=pg.mkBrush(255, 255, 255, 80))
    pos = np.random.normal(size=(2,n), scale=1e-5)
    spots = [{'pos': pos[:,i], 'data': 1} for i in range(n)] + [{'pos': [0,0], 'data': 1}]
    s1.addPoints(spots)
    w1.addItem(s1)
    
    # Add label to GraphicsLayoutWidget
    l1 = view.addLabel('CELLS',row=10,col=20)
    
    s1.sigClicked.connect(clicked)
    
if win2:
    w2 = view.addPlot()
    s2 = pg.ScatterPlotItem(size=10, pen=pg.mkPen('w'), pxMode=True)
    pos = np.random.normal(size=(2,n), scale=1e-5)
    spots = [{'pos': pos[:,i], 'data': 1, 'brush':pg.intColor(i, n), 
              'symbol': i%5, 'size': 5+i/10.} for i in range(n)]
    s2.addPoints(spots)
    w2.addItem(s2)
    s2.sigClicked.connect(clicked)
    
if win3:
    w3 = view.addPlot()
    s3 = pg.ScatterPlotItem(pxMode=False)   ## Set pxMode=False to allow spots to transform with the view
    spots3 = []
    for i in range(10):
        for j in range(10):
            spots3.append({'pos': (1e-6*i, 1e-6*j), 'size': 1e-6, 'pen': {'color': 'w', 'width': 2}, 'brush':pg.intColor(i*10+j, 100)})
    s3.addPoints(spots3)
    w3.addItem(s3)
    s3.sigClicked.connect(clicked)


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

'''