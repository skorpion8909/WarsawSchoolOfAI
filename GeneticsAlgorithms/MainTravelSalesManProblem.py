
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
    manager.startTraining(event)
def addChangerListiner(manager,app,event):
    thread = t.Thread(target = changeListiner, args = (manager,app,event,))
    thread.start()
def changeListiner(manager,app,event):
    lastBest = None
    best = None
    print("Starting listiner thread")
    while True:
        print("x")
        event.wait()
        lastBest, best = best,manager.population.bestSalesman
        if lastBest is not best:
            app.getCurrentTopFrame().updateFrame(best.dna.getAsListOfTuple())
        event.clear()
if __name__ == "__main__":
#     listOfCities = [(631, 44), (612, 137), (441, 266), (447, 173), (52, 243), (104, 148), (333, 70), (474, 182), (419, 221), (238, 291), (264, 340), (290, 213), (332, 97), (473, 294), (188, 198), (180, 258), (433, 382), (394, 139)]
    listOfCities = rmg.genRandomListOfPoints(15,800,400)
    pop = Population.Population(400,listOfCities)
    manager = EvolutionManager.EvolutionManager(100,pop)
    event = mp.Event()
    pro = t.Thread(target = genethicAlgorithmPart, args = (event,manager))
    app = MainFrame.MainFrame()
    app.getCurrentTopFrame().updateFrame(manager.population.bestSalesman.dna.getAsListOfTuple())
    app.after(111, addChangerListiner(manager, app, event))
    pro.start()
    app.mainloop()
#-------------------------------------------------------------------------------------
