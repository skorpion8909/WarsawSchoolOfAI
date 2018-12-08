
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






class InitFrame:
    """ This class contains all function to start training different algo in seperate windows"""
#-------------------------------------------------------------------------------------     
    def __init__(self,listOfPoints, popSize, algoType):
        listOfCities = listOfPoints
        pop = Population.Population(1011,listOfCities)
        self.manager = EvolutionManager.EvolutionManager(100,pop,algoType)
        self.event = mp.Event()
        pro = t.Thread(target = self.genethicAlgorithmPart)
        self.app = MainFrame.MainFrame()
        self.app.setForClosingEvent(self.manager)
        pro.start()
        self.app.after(111, self.addChangerListiner())
        self.app.mainloop()
        print("asda")
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


if __name__ == "__main__":
    listOfCities = rmg.genRandomListOfPoints(40,800,400)
    t= InitFrame(listOfCities, 100, "pmx")
    
    
    