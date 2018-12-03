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
#-------------------------------------------------------------------------------------     
class MainFrame(tk.Tk):
    """ This is main class for managing different views(windows) """
    def __init__(self, *args, **kwargs):
        
        # for notifing that Tkiner is 100% loaded
        self.mainFrameIsVisible = False
        
        tk.Tk.__init__(self, *args, **kwargs)
        # init main frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = CanvasFrame.CanvasFrame(container, self)

        self.frames[CanvasFrame] = frame

        frame.grid(row=0, column=0, sticky="nsew")
        # load canvas
        self.show_frame(CanvasFrame)
        print("After main loop")
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
    
