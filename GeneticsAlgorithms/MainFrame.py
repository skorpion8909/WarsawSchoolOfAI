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
        sys.exit()
#-------------------------------------------------------------------------------------   
    def setEvent(self,event):
        self.event = event
#-------------------------------------------------------------------------------------     
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # init main frame
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand = True)
#         self.container.grid(row = 0, column = 0, sticky = "nswe")
        self.frames = {}
        # init frame add to dict
        frame = CanvasFrame.CanvasFrame(self.container, self)
        self.frames[CanvasFrame] = frame
        frame.grid(row = 0, column = 0, sticky = "nswe")
         # init frame add to dict
        frame = StartFrame.StartFrame(self.container, self)
        self.frames[StartFrame] = frame
        frame.grid(row = 0, column = 0, sticky = "nswe")
         # add close window event handler
        self.protocol("WM_DELETE_WINDOW", self.onClossing)
        # load canvas
        self.show_frame(StartFrame)
#------------------------------------------------------------------------------------- 
    def show_frame(self, cont):
        """ makes choosen frame visibale at top"""
        # get window
        frame = self.frames[cont]
        
        self.topFrame = frame
        # make window in front
        # .lift() should also works
#         self.attributes("-topmost", True)
        frame.tkraise()
        # set gird position
        print("Show Frame")
#-------------------------------------------------------------------------------------     
    def getCurrentTopFrame(self):
        """ returns top frame object"""
        return self.topFrame
#-------------------------------------------------------------------------------------     
    def setForClossingEvent(self, manager):
        """ sets thread variable for future stoping when app is being closed"""
        self.manager = manager
#-------------------------------------------------------------------------------------     \
    def genethicAlgorithmPart(self):
        """begins the training sequence"""
        self.manager.startTraining()
#-------------------------------------------------------------------------------------   
    def addChangerListiner(self):
        """ makes a new thread in widget process to monitor changes to be displayed"""
        thread = t.Thread(target = self.changeListiner)
        thread.start()
#-------------------------------------------------------------------------------------   
    def changeListiner(self):
        """ contains logic for cheking for changes and updatting them"""
        lastBest = None
        best = None
        print("Starting listiner thread")
        while True:
            #wait for info about event
            self.event.wait()
            #get new possible best one and old one store for future comparing
            lastBest, best = best,self.manager.population.bestSalesman
            if lastBest is not best:
                # if new one is really better then update the drawing on canvas
                self.getCurrentTopFrame().updateFrame(best.dna.getAsListOfTuple())
            # clear event so it could be set again
            self.event.clear()
#-------------------------------------------------------------------------------------           
