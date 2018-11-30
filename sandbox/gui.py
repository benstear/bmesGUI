#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:37:30 2018

@author: benstear
"""

import numpy as np
import tkinter
import matplotlib.pyplot as plt
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("we will analyze your single-cell data shortly!")
        x = range(0,100)
        y = np.sin(x)
        plt.plot(x,y)
        plt.show()


##################################
root = tk.Tk()
app = Application(master=root)
app.mainloop()

