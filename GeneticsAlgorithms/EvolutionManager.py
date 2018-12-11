"""
    
    This class governs process of looking for better
    combination making a path for a traveler
    

"""
import Population
import multiprocessing as mp
import time
import operator
import RandomMapGenerator as rmg
import threading as t
import CanvasFrame
#-------------------------------------------------------------------------------------------
class EvolutionManager:
    def checkPopulationSize(self):
        """ make sure population size is event"""
        # if odd
        if self.populationSizeVal % 2 != 0:
            # add one
            self.populationSizeVal += 1
#-------------------------------------------------------------------------------------------
    def __init__(self, numOfPointsVal, populationSizeVal, rootWindow, controller):
        """Takes number of generations and Population() object"""
        self.pause = True
        self.stop = False
        # get random list
        listOfCities = rmg.genRandomListOfPoints(numOfPointsVal,800,400)
        # how often will mutation occur
        self.mutateRate = 0.15
        # not use
        self.mutateChance = 1
        self.populationSizeVal = populationSizeVal
        # population size must be even
        self.checkPopulationSize()
        
        self.population = population = Population.Population(self.populationSizeVal,listOfCities, self.mutateChance, self.mutateRate)
        self.event = mp.Event()
        controller.setEvent(self.event)
        controller.setForClossingEvent(self)
        pro = t.Thread(target = controller.genethicAlgorithmPart)
        pro.start()
        rootWindow.after(300,controller.addChangerListiner())
        controller.show_frame(CanvasFrame)
        controller.getCurrentTopFrame().updateFrame(self.population.bestSalesman.dna.getAsListOfTuple())
        print("After init EvolutionManager")
#-------------------------------------------------------------------------------------------
    def displayPopulation(self):
        salesmanList = self.population.salesmanList
        sorted_salesmanList = sorted(salesmanList, key=operator.attrgetter('distance'))
#         for x in sorted_salesmanList:
#             string = ""
#             distance = str(x.distance)
#             print(distance)
#             string = string + " "+ distance
        co = 0
        print("Best one ever",self.population.bestSalesman.distance)
        print("Best from pop -->",sorted_salesmanList[0].distance)
#-------------------------------------------------------------------------------------------
    def startTraining(self):
        """Starts training sequence"""
        x = 0
        self.pause = False
        while not self.stop:
            while not self.pause and not self.stop:
#                 for x in range(0,self.numOfGenerations):
                # generate next population
                self.population.nextGeneration()
                # display on consol info about new population
                self.displayPopulation()
              # notify about new best solution
                self.event.set()
                print("Iteration num ",x,"Fitness of best one is ",self.population.bestSalesman)
#             self.canvas.updateFrame(self.population.bestSalesman.dna.getAsListOfTuple())
                if x == 10000:
                    self.stop = True;
                x += 1
                if self.stop:
                    break
            if self.stop:
                break
#-------------------------------------------------------------------------------------------
    def getList(self, li):
        print(li)
        listToReturn = list()
        for x in li:
            listToReturn.append((x.tupleXY[0],x.tupleXY[1]))
        return listToReturn
#-------------------------------------------------------------------------------------------
    def pauseMainLoop(self):
        """ pause main loop"""
        self.pause= True
#-------------------------------------------------------------------------------------------
    def startMainLoop(self):
        """ start main loop"""
        self.pause = False
#-------------------------------------------------------------------------------------------
    def stopMainLoop(self):
        """ stop main loop"""
        self.stop = True
#-------------------------------------------------------------------------------------------


