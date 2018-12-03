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
#-------------------------------------------------------------------------------------     
def di(p1,p2):
    """ returns distance between points"""
    return (m.sqrt(m.pow(p1[0] - p2[0],2)) + m.pow((p1[1] - p2[1]),2))
#-------------------------------------------------------------------------------------     
def genRandomListOfPoints(sizeOfList,height,width):
    """ returns list with random points in range of window as tuple"""
    listToReturn = list()
    minimumDistance = 5
    he = height - 10
    wi = width - 10
    notValidPoint = True
    distanceIsCorrect = False
    while len(listToReturn) < 10:
        while notValidPoint:
            randomPoint = (r.randint(10,he),r.randint(10,wi))
            if len(listToReturn) == 0:
                listToReturn.append(randomPoint)
                break
            for p in listToReturn:
                if di(randomPoint,p) >= 5:
                    distanceIsCorrect = True
                else:
                    distanceIsCorrect = False
            if distanceIsCorrect:
                listToReturn.append(randomPoint)
                break
        print(len(listToReturn))
    return listToReturn
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
def changeListiner(manager,app,event):
    lastBest = None
    best = None
    while True:
        print("x")
        event.wait()
        lastBest, best = best,manager.population.bestSalesman
        if lastBest is not best:
            app.getCurrentTopFrame().updateFrame(best.dna.getAsListOfTuple())
        event.clear()
    
if __name__ == "__main__":
    listOfCities = [(0,121),(112,5),(14,201),(45,88),(141,231),(1,8),(22,11),(101,84),(90,231)]
    pop = Population.Population(200,listOfCities)
    manager = EvolutionManager.EvolutionManager(100,pop)
    event = mp.Event()
    pro = t.Thread(target = genethicAlgorithmPart, args = (event,manager,))
    pro.start()
    app = MainFrame()
    app.getCurrentTopFrame().updateFrame(manager.population.bestSalesman.dna.getAsListOfTuple())
    app.mainloop()
    app.after(1111, changeListiner(manager, app, event))
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
