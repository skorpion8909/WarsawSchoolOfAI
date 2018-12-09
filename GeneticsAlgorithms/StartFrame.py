"""
    This class contains all functions to init start of different windows
    based on choosen starting options

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
class StartFrame(tk.Frame):
    """ This is main class for starting different windows based on choosen options"""
#-------------------------------------------------------------------------------------     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.rootWindow = parent
        self.controller = controller
        # init main frame
        self.controller = controller
        container = tk.Frame(self, width=500, height=300)
#         container.pack(side="top", fill="both", expand = True)
        # stores starting options
        self.checkBoxDict = dict()
        
        # add start info
        entryInfo = tk.Label(text = "Choose your settings, one window running different algorithm will be open for every check box checked")
        # columnspan is used to allow components be better spaced between each other
        entryInfo.pack()
        # add rest of controlers
        self.addControlers()
#-------------------------------------------------------------------------------------     
    def addControlers(self):
        """sets rest of gui"""
        info = tk.Label(text = "Choose what algorithms(crossover) you want to compare")
        info.pack()
        
        textAreaLabel1 = tk.Label(text = "How big population ? (best 100-500)")
        textAreaLabel1.pack()
        self.populationSize = tk.Entry()
        self.populationSize.pack()
       
        textAreaLabel2 = tk.Label(text = "How many points ? (best 20-50)")
        textAreaLabel2.pack()
        
        self.numOfPoints = tk.Entry()
        self.numOfPoints.pack()
       
        self.checkBoxDict["ramdom"] = tk.BooleanVar()
        checkButton1 = tk.Checkbutton( text="Pure randomness approach", variable=self.checkBoxDict["ramdom"])
        checkButton1.pack()
        checkButton1.config(state='disabled')
        
        self.checkBoxDict["pmx"] = tk.BooleanVar()
        checkButton2 = tk.Checkbutton( text="PMX crossover", variable=self.checkBoxDict["pmx"])
        checkButton2.pack()
        
        self.checkBoxDict["mutation"] = tk.BooleanVar()
        checkButton3 = tk.Checkbutton( text="Only mutation no crossover", variable=self.checkBoxDict["mutation"]   )
        checkButton3.pack()
        checkButton3.config(state='disabled')
        
        self.startButton = tk.Button(text = "Start", bd = 3, bg = "#20aa20", command = lambda:self.start())
        self.startButton.pack()
#-------------------------------------------------------------------------------------
    def start(self):
        """inits comparison of choosen functions"""
        # cheks if corrent value is inserted
        try:
            self.populationSizeVal = int(self.populationSize.get())
        except ValueError:
            # if is not then notify that
            self.populationSize.delete(0,tk.END)
            self.populationSize.insert(0,"This was not an INT!")
        # cheks if corrent value is inserted
        try:
            self.numOfPointsVal = int(self.numOfPoints.get())
        except ValueError:
            # if is not then notify that
            self.numOfPoints.delete(0,tk.END)
            self.numOfPoints.insert(0,"This was not an INT!")
        
        if self.checkBoxDict["pmx"].get():
            self.run()
#-------------------------------------------------------------------------------------     
    def run(self):
        listOfCities = rmg.genRandomListOfPoints(self.numOfPointsVal,800,400)
        mutateChance = 0.10
        mutateRate = 0.01
        pop = Population.Population(self.populationSizeVal,listOfCities, mutateChance, mutateRate)
        manager = EvolutionManager.EvolutionManager(300,pop)
        event = mp.Event()
        self.controller.setEvent(event)
        self.controller.setForClossingEvent(manager)
        pro = t.Thread(target = self.controller.genethicAlgorithmPart)
        pro.start()
        self.rootWindow.after(300,self.controller.addChangerListiner())
        self.controller.show_frame(CanvasFrame)
        self.controller.getCurrentTopFrame().updateFrame(pop.bestSalesman.dna.getAsListOfTuple())
        self.startButton.config(state = "disabled")
        
        