"""
    This class contains all functions to graphically display progress in a window
    and manage different settings.
    
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

        frame = CanvasFrame(container, self)

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
class CanvasFrame(tk.Frame):
    """ This is main class for managing displaying visual changes to a path"""
#-------------------------------------------------------------------------------------     
    def __init__(self, parent, controller):
        self.rootWindow = controller
        tk.Frame.__init__(self,parent)
        wid = 800
        hei = 400
        self.canvas = tk.Canvas(self, width = wid, height = hei)
        self.canvas.pack()
#-------------------------------------------------------------------------------------     
    def start(self):
#         pro = Process( target = self.manager.startTraining(), args = ())
#         pro.start()
        # deley in secound
        deley = 2
        print("Before logic thread init")
        lock = mp.Lock()
#         pool = mp.Pool()
#         pool.apply(target = self.manager.startTraining(lock))
#         pool.start()
#         threading.Thread(target = self.startWithDeley(deley,lock)).start()
        pro = mp.Process(target = self.manager.startTraining, args = (deley,lock, ))
        pro.start()
 #-------------------------------------------------------------------------------------     
    def updateFrame(self,listOfPoints):
        """ draws all points"""
        self.canvas.delete("all")
        for y in listOfPoints:
            self.canvas.create_oval(y[0], y[1], y[0]+5, y[1]+5, fill="Black")
        li = cycle(listOfPoints)
        p2 = next(li)
        for x in listOfPoints:
            p1,p2 = p2, next(li)
            self.canvas.create_line(p1[0],p1[1],p2[0]+2,p2[1]+2)
            if p2 == listOfPoints[-1]:
                self.canvas.create_line(p2[0],p2[1],listOfPoints[0][0]+2,listOfPoints[0][1]+2)
        self.canvas.pack()
#-------------------------------------------------------------------------------------     
def genethicAlgorithmPart(event, manager):
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
    pro = t.Thread(target = genethicAlgorithmPart, args = (event,manager,))
    app = MainFrame()
    app.getCurrentTopFrame().updateFrame(manager.population.bestSalesman.dna.getAsListOfTuple())
    app.after(111, addChangerListiner(manager, app, event))
    pro.start()
    app.mainloop()
#-------------------------------------------------------------------------------------     
def mains(list):
    hei = 300
    wid = 400
    tk = Tk()
    canvas = Canvas(tk, width = wid, height = hei)
    pointsList = list
    x = 10
    print(pointsList)
    for y in pointsList:
        canvas.create_oval(y[0], y[1], y[0]+5, y[1]+5, fill="Black")
        x += 10
    li = cycle(pointsList)
    p2 = next(li)
    for x in pointsList:
        p1,p2 = p2, next(li)
        canvas.create_line(p1[0],p1[1],p2[0]+2,p2[1]+2)
        if p2 == pointsList[-1]:
            canvas.create_line(p2[0],p2[1],pointsList[0][0]+2,pointsList[0][1]+2)
    canvas.pack()
    tk.mainloop()
# main()
    
