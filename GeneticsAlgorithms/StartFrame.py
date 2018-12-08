"""
    This class contains all functions to init start of different windows
    based on choosen starting options

"""
import os
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
import RandomMapGenerator as rmg
import MainFrame
import subprocess
#-------------------------------------------------------------------------------------     
class StartFrame(tk.Tk):
    """ This is main class for starting different windows based on choosen options"""
#-------------------------------------------------------------------------------------     
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # init main frame
        container = tk.Frame(self, width=500, height=300)
#         container.pack(side="top", fill="both", expand = True)
        # stores starting options
        self.checkBoxDict = dict()
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(2, weight=1)

        # add start info
        entryInfo = tk.Label(text = "Choose your settings, one window running different algorithm will be open for every check box checked")
        # columnspan is used to allow components be better spaced between each other
        entryInfo.grid(row = 0, column = 0, columnspan=10)
        # add rest of controlers
        self.addControlers()
        print("")
#-------------------------------------------------------------------------------------     
    def addControlers(self):
        """sets rest of gui"""
        info = tk.Label(text = "Choose what algorithms(crossover) you want to compare")
        info.grid(row = 1, column = 0, sticky="w", columnspan=10)
        
        textAreaLabel1 = tk.Label(text = "How big population ? (best 100-500)")
        textAreaLabel1.grid(row = 3, column = 0, sticky="w")
       
        self.populationSize = tk.Entry()
        self.populationSize.grid(row = 3, column = 1,sticky="w")
       
        textAreaLabel2 = tk.Label(text = "How many points ? (best 20-50)")
        textAreaLabel2.grid(row = 4, column = 0, sticky="w")
        
        self.numOfPoints = tk.Entry()
        self.numOfPoints.grid(row = 4, column = 1, sticky="W")
       
        self.checkBoxDict["ramdom"] = tk.BooleanVar()
        checkButton1 = tk.Checkbutton( text="Pure randomness approach", variable=self.checkBoxDict["ramdom"])
        checkButton1.grid(row = 5, column = 0, sticky="W")
        
        self.checkBoxDict["pmx"] = tk.BooleanVar()
        checkButton2 = tk.Checkbutton( text="PMX crossover", variable=self.checkBoxDict["pmx"])
        checkButton2.grid(row = 6, column = 0, sticky="W")
        
        self.checkBoxDict["mutation"] = tk.BooleanVar()
        checkButton3 = tk.Checkbutton( text="Only mutation no crossover", variable=self.checkBoxDict["mutation"]   )
        checkButton3.grid(row = 7, column = 0, sticky="W")
        
        startButton = tk.Button(text = "Start", bd = 3, bg = "#20aa20", command = lambda:self.start())
        startButton.grid(row = 8, sticky = "nswe", columnspan=10)
#-------------------------------------------------------------------------------------
    def start(self):
        """inits comparison of choosen functions"""
        # cheks if corrent value is inserted
        correct = True
        try:
            self.populationSizeVal = int(self.populationSize.get())
        except ValueError:
            # if is not then notify that
            self.populationSize.delete(0,tk.END)
            self.populationSize.insert(0,"This was not an INT! 1 will make bug")
            correct = False
        # cheks if corrent value is inserted
        try:
            self.numOfPointsVal = int(self.numOfPoints.get())
        except ValueError:
            # if is not then notify that
            self.numOfPoints.delete(0,tk.END)
            self.numOfPoints.insert(0,"This was not an INT! PS. 1 will make bug")
            correct = False
        if correct:
            listOfCities = rmg.genRandomListOfPoints(self.numOfPointsVal,800,400)
            for algoType, isChoosen in self.checkBoxDict.items():
                if isChoosen.get():
                    print(algoType)
                    p = mp.Process(target = self.run(listOfCities,  self.populationSizeVal, algoType))
                    p.start()
            # close this window, it is longer no necessary
#-------------------------------------------------------------------------------------
    def run(self, listOfCities, populationSizeVal, algoType):
        """ Starts other window from new process"""
        filePath = os.path.dirname(os.path.realpath(__file__))
        command = f"python {filePath}/Test.py {listOfCities} {populationSizeVal} {algoType}"
        print(command)
        subprocess.Popen(command)
#-------------------------------------------------------------------------------------     
class InitFrame:
    """ This class contains all function to start training different algo in seperate windows"""
#-------------------------------------------------------------------------------------     
    def __init__(self,listOfPoints, popSize, algoType):
        listOfCities = listOfPoints
        pop = Population.Population(popSize,listOfCities)
        self.manager = EvolutionManager.EvolutionManager(pop,algoType)
        self.event = mp.Event()
        pro = t.Thread(target = self.genethicAlgorithmPart)
        self.app = MainFrame.MainFrame()
        self.app.setForClosingEvent(self.manager)
        pro.start()
        self.addChangerListiner()
        self.app.mainloop()
#-------------------------------------------------------------------------------------     
    def genethicAlgorithmPart(self):
        """ begins the training sequence"""
        self.manager.startTraining(self.event)
#-------------------------------------------------------------------------------------     
    def addChangerListiner(self):
        """ makes a new thread in widget process to monitor changes to be displayed"""
        thread = t.Thread(target = self.changeListiner(), args = (self,))
        thread.start()
#-------------------------------------------------------------------------------------     
    def changeListiner(self):
        """ contains logic for cheking for changes and updatting them"""
        lastBest = None
        best = None
        while True:
            #wait for info about event
            self.event.wait()
            #get new possible best one and old one store for future comparing
            lastBest, best = best,self.manager.population.bestSalesman
            if lastBest is not best:
                # if new one is really better then update the drawing on canvas
                self.app.getCurrentTopFrame().updateFrame(best.dna.getAsListOfTuple())
            # clear event so it could be set again
            self.event.clear()
#-------------------------------------------------------------------------------------     
