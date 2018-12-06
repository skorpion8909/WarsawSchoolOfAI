"""
    This class contains all functions to manage different windows
    
    Base line for this code is from Sentdex(link under)
    https://pythonprogramming.net/object-oriented-programming-crash-course-tkinter/

"""

import random as r
from itertools import cycle
import tkinter as tk
import EvolutionManager
import Population
import multiprocessing as mp
import time
import threading as t
import RandomMapGenerator as rmg
import CanvasFrame
import sys
#-------------------------------------------------------------------------------------     
class MainFrame(tk.Tk):
    """ This is main class for managing different views(windows) """
    def onClosing(self):
        self.destroy()
        self.manager.stopMainLoop()
#-------------------------------------------------------------------------------------     
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # init main frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # init frames dict
        self.frames = {}
        # init canvas
        frame = CanvasFrame.CanvasFrame(container, self)
        # add frame to frames dict
        self.frames[CanvasFrame] = frame
        # expend frame
        frame.grid(row=0, column=0, sticky="nsew")
        # add close window event handler
        self.protocol("WM_DELETE_WINDOW", self.onClosing)
        # load canvas
        self.show_frame(CanvasFrame)
    def getCurrentTopFrame(self):
        return self.frames[CanvasFrame]
#-------------------------------------------------------------------------------------     
    def show_frame(self, cont):
        # add class to map
        frame = self.frames[cont]
        # move canvas to front
        frame.tkraise()
        print("After tkrasie")
        print("after start")
#-------------------------------------------------------------------------------------     
    def setForClosingEvent(self, manager):
        """ sets thread variable for future stoping when app is being closed"""
        self.manager = manager
#-------------------------------------------------------------------------------------     
    
