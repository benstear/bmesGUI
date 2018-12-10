#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:15:43 2018

@author: dawnstear
"""
import cv2

class videowidget():
    def __init__(self, videofilepath):
        self.vidpath = videofilepath
            
    # https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
    def display_video(self):
        cap = cv2.VideoCapture(self.vidpath)
        while(cap.isOpened()):
            ret, self.frame = cap.read()
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',gray)
            if cv2.waitKey(60) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        
    def getframe(self):
        return self.frame
    
    
    
'''
# Call function
vidfile = '/Users/dawnstear/desktop/GOPR1457.MP4'    
myvid = videowidget(vidfile)
myvid.display_video()
myframe = myvid.getframe()
print(myframe)
'''