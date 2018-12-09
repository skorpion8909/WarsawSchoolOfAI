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
import StartFrame
#-------------------------------------------------------------------------------------     
class MainFrame(tk.Tk):
    """ This is main class for managing different views(windows) """
    def onClosing(self):
        self.manager.stopMainLoop()
        self.destroy()
#-------------------------------------------------------------------------------------     
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # init main frame
        container = tk.Frame(self)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
#         frame = StartFrame.StartFrame(container, self)
#         self.frames[StartFrame] = frame
#         frame.grid(row = 0, column = 0, sticky = "nwse")

        frame = CanvasFrame.CanvasFrame(container, self)
        self.frames[CanvasFrame] = frame
        frame.grid(row = 0, column = 0, sticky = "nwse")
        
        # add close window event handler
        self.protocol("WM_DELETE_WINDOW", self.onClosing)
        # load canvas
        self.show_frame(CanvasFrame)
#------------------------------------------------------------------------------------- 
    def getCurrentTopFrame(self):
        """ returns top frame object"""
        return self.topFrame
#-------------------------------------------------------------------------------------     
    def show_frame(self, cont):
        # add class to map
        frame = self.frames[cont]
        print(frame)
        # move canvas to front
        print("Tk trise Przed")
        # self.topFrame.lift() should also works
        frame.tkraise()
        print("po")
#-------------------------------------------------------------------------------------     
    def setForClosingEvent(self, manager):
        """ sets thread variable for future stoping when app is being closed"""
        self.manager = manager
#-------------------------------------------------------------------------------------     
    
