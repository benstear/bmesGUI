#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:31:22 2018

@author: dawnstear
"""

import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QLabel, QGridLayout,QDockWidget, QWidget, QPlainTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
from videowidget import videowidget
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from utilities import load, myselect, create_db, view_db

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 400))    
        self.setWindowTitle("Neuroergonomic Wheelchair Control Retrospective GUI") 
        
        #self.w = pg.GraphicsWindow()
        #self.centerplot = QMainWindow.setCentralWidget(self,pg.PlotWidget())
        '''
        self.layout = QHBoxLayout()
        myplot = pg.PlotWidget()
        layout.addWidget(my_plot)
        my_plot.plot(x, y)
        
        
        self.items = QDockWidget("fNRI plot", self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        
        my_plot = pg.PlotWidget()
        layout.addWidget(my_plot)
        my_plot.plot(x, y) '''
        
        
        # Annotation Box
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("Annotate video here.\n")
        self.b.move(330,30)
        self.b.resize(160,200)
        
        # Database query Box
        self.q = QPlainTextEdit(self)
        self.q.insertPlainText("Query database.\n")
        self.q.move(170,30)
        self.q.resize(160,200)
        
        
        # Define places to keep track of logs
        self.errors = []
        self.inclines = []
        self.bumps = []
        self.slopes = []
        self.annotations = []
        self.cones = []
        self.cwd = os.getcwd()
        h=250

        # Define names/format of buttons          
        bumpbtn = QPushButton('Record Bump', self)
        bumpbtn.clicked.connect(self.bump_btn_clicked)
        bumpbtn.resize(128,50)
        bumpbtn.move(20, 30)  
        
        slopebtn = QPushButton('Record Slope', self)
        slopebtn.clicked.connect(self.bump_btn_clicked)
        slopebtn.resize(128,50)
        slopebtn.move(20, 80)  
        
        inclinebtn = QPushButton('Record Incline', self)
        inclinebtn.clicked.connect(self.slope_btn_clicked)
        inclinebtn.resize(128,50)
        inclinebtn.move(20, 135) 
        
        errorbtn = QPushButton('Record Error', self)
        errorbtn.clicked.connect(self.error_btn_clicked)
        errorbtn.resize(128,50)
        errorbtn.move(20, h)
        
        querybtn = QPushButton('Query', self)
        querybtn.clicked.connect(self.query_btn_clicked)
        querybtn.resize(128,50)
        querybtn.move(185,h) 
        
        annotatebtn = QPushButton('Submit', self)
        annotatebtn.clicked.connect(self.annotate_btn_clicked)
        annotatebtn.resize(128,50)
        annotatebtn.move(350, h)
        
        savebtn = QPushButton('Save', self)
        savebtn.clicked.connect(self.save_btn_clicked)
        savebtn.resize(128,50)
        savebtn.move(185, 320)
        
        conebtn = QPushButton('Record Cone', self)
        conebtn.clicked.connect(self.cone_btn_clicked)
        conebtn.resize(128,50)
        conebtn.move(20,190) 

        
        # =========Define button on_click functions========= #
    def error_btn_clicked(self):       
        print('error')
        frame = videowidget.getframe()
        self.errors.append('Error recorded at frame: %s' % frame)
        
    def bump_btn_clicked(self):
        print('bump')
        frame = videowidget.getframe()
        self.bumps.append('Bump recorded at frame: %s ' %  frame)
        
    def slope_btn_clicked(self):
        print('slope')
        frame = videowidget.getframe()
        self.slopes.append('Slope recorded at frame: %s ' % frame)
        
    def incline_btn_clicked(self):
        print('incline')
        frame = videowidget.getframe()
        self.inclines.append('Incline recorded at frame: %s ' % frame)
        
    def cone_btn_clicked(self):
        print('cone')
        frame = videowidget.getframe()
        self.cones.append('Cone recorded at frame: %s ' % frame)
        
    def annotate_btn_clicked(self):
        annotation_text = self.b.toPlainText() 
        print(annotation_text)
        frame = videowidget.getframe()
        self.annotations.append('Annotation for frame %s: %s' % (frame,annotation_text))
        self.b.clear()

     # -----------------------------------------#
    def query_btn_clicked(self):
        query = self.q.toPlainText()
        queryresults = myselect(query)
        print(queryresults)
        
    def save_btn_clicked(self,filename):
        filename='logfile'
        directory = self.cwd+'/'+filename
        
        if filename is not None and not os.path.isfile(directory):
            f = open(directory,'w')
            f.write('\t\t\t\t ----------Log File---------\n\n\n')
            f.write('Errors:\n\n')
            f.write(self.errors+'\n\n')
            f.write('Bumps:\n\n')
            f.write(self.bumps+'\n\n')
            f.write('Inclines: \n\n')
            f.write(self.inclines+'\n\n')
            f.write('Slopes: \n\n')
            f.write(self.slopes+'\n\n')
            f.write('Annotations: \n\n')
            f.write(self.annotations)
            f.close
        else:
            print('Filename Not Specified')
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()    
    sys.exit( app.exec_() )
    #vidfile = '/Users/dawnstear/desktop/GOPR1457.MP4'    
    #myvid = videowidget(vidfile)
    #myvid.display_video()
    
    