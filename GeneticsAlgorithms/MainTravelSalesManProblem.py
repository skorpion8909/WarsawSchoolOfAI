
"""
    ******************************************************************
    *                                                                *
    * Travel Sales Man problem is a type of problem where we can use *
    * genethic algorithm to find better and faster answer.          *
    *                                                                *
    ******************************************************************
    
    1.) This class is main class for this project

"""
import Population
import EvolutionManager
import random as r
import tkinter as tk
import EvolutionManager
import Population
import multiprocessing as mp
import time
import threading as t
import RandomMapGenerator as rmg
import MainFrame

#-------------------------------------------------------------------------------------
def genethicAlgorithmPart(event,manager):
    """begins the training sequence"""
    manager.startTraining(event)
def addChangerListiner(manager,app,event):
    """ makes a new thread in widget process to monitor changes to be displayed"""
    thread = t.Thread(target = changeListiner, args = (manager,app,event,))
    thread.start()
def changeListiner(manager,app,event):
    """ contains logic for cheking for changes and updatting them"""
    lastBest = None
    best = None
    print("Starting listiner thread")
    while True:
        print("x")
        #wait for info about event
        event.wait()
        #get new possible best one and old one store for future comparing
        lastBest, best = best,manager.population.bestSalesman
        if lastBest is not best:
            # if new one is really better then update the drawing on canvas
            app.getCurrentTopFrame().updateFrame(best.dna.getAsListOfTuple())
        # clear event so it could be set again
        event.clear()
if __name__ == "__main__":
#     listOfCities = [(631, 44), (612, 137), (441, 266), (447, 173), (52, 243), (104, 148), (333, 70), (474, 182), (419, 221), (238, 291), (264, 340), (290, 213), (332, 97), (473, 294), (188, 198), (180, 258), (433, 382), (394, 139)]
    app = MainFrame.MainFrame()
    app.mainloop()
#-------------------------------------------------------------------------------------




