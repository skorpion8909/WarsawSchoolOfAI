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
    def onClossing(self):
        self.manager.stopMainLoop()
        self.destroy()
#-------------------------------------------------------------------------------------     
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # init main frame
        container = tk.Frame(self)
        container.grid(row = 0, column = 0, sticky = "nwse")
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
         
        # init dict for storing avaliable frames
        self.frames = {}
        # init frame add to dict
        frame = CanvasFrame.CanvasFrame(container, self)
        self.frames[CanvasFrame] = frame
        
        # init frame add to dict
        frame = StartFrame.StartFrame(container, self)
        self.frames[StartFrame] = frame

        
        # add close window event handler
        self.protocol("WM_DELETE_WINDOW", self.onClossing)
        # load canvas as first
        self.show_frame(CanvasFrame)
#------------------------------------------------------------------------------------- 
    def show_frame(self, cont):
        """ makes choosen frame visibale at top"""
        # get window
        self.topFrame = self.frames[cont]
        # .lift() should also works
        # make window in front
        self.topFrame.tkraise()
        # set gird position
#-------------------------------------------------------------------------------------     
    def getCurrentTopFrame(self):
        """ returns top frame object"""
        return self.topFrame
#-------------------------------------------------------------------------------------     
    def setForClossingEvent(self, manager):
        """ sets thread variable for future stoping when app is being closed"""
        self.manager = manager
#-------------------------------------------------------------------------------------     
    
