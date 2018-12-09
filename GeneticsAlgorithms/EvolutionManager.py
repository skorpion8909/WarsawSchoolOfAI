"""
    
    This class governs process of looking for better
    combination making a path for a traveler
    

"""
import Population
import multiprocessing as mp
import time
import operator
#-------------------------------------------------------------------------------------------
class EvolutionManager:
    def __init__(self, numOfGenerations,population):
        """Takes number of generations and Population() object"""
        self.numOfGenerations = numOfGenerations
        self.population = population
        self.pause = False
        self.stop = False
        print("After init EvolutionManager")
#-------------------------------------------------------------------------------------------
    def displayPopulation(self):
        salesmanList = self.population.salesmanList
        sorted_salesmanList = sorted(salesmanList, key=operator.attrgetter('distance'))
#         for x in sorted_salesmanList:
#             string = ""
#             distance = str(x.distance)
#             string = string + " "+ distance
        co = 0
        for x in sorted_salesmanList:
            print(sorted_salesmanList[len(sorted_salesmanList)-co-1].distance)
            co += 1
            print(co)
        print("Best one ever",self.population.bestSalesman.distance)
        print("Best from pop -->",sorted_salesmanList[0].distance)
#-------------------------------------------------------------------------------------------
    def startTraining(self,event):
        """Starts training sequence"""
        x = 0
        while not self.stop:
            while not self.pause and not self.stop:
#                 for x in range(0,self.numOfGenerations):
                # generate next population
                self.population.nextGeneration()
                # display on consol info about new population
                self.displayPopulation()
              # notify about new best solution
                event.set()
                print("Iteration num ",x,"Fitness of best one is ",self.population.bestSalesman)
#             self.canvas.updateFrame(self.population.bestSalesman.dna.getAsListOfTuple())
                if x == 1000000:
                    self.stop = True;
                x += 1
                print(self.stop)
#-------------------------------------------------------------------------------------------
    def getList(self, li):
        print(li)
        listToReturn = list()
        for x in li:
            listToReturn.append((x.tupleXY[0],x.tupleXY[1]))
        return listToReturn
#-------------------------------------------------------------------------------------------
    def stopMainLoop(self):
        """ sets stop to True for ending mainloop"""
        self.stop = True


