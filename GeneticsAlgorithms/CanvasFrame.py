
"""
    This class contains all code to graphically display progress in a window.
    
"""

import random as r
from itertools import cycle
import tkinter as tk

class CanvasFrame(tk.Frame):
    """ This is main class for managing displaying visual changes to a path"""
#-------------------------------------------------------------------------------------     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.rootWindow = controller
        wid = 800
        hei = 400
        self.canvas = tk.Canvas(self, width = wid, height = hei)
        self.canvas.grid(row = 0, column = 0, columnspan = 10,sticky = "nswe")
#         self.canvas.pack(side = "top", fill = "both", expand = True)
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