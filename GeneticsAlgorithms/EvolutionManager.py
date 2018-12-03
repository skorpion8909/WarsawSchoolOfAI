"""
    
    This class governs process of looking for better
    combination making a path for a traveler
    

"""
import Population
import MainFrame
import multiprocessing as mp
import time
#-------------------------------------------------------------------------------------------
class EvolutionManager:
    def __init__(self, numOfGenerations,population):
        """Takes number of generations and Population() object"""
        self.numOfGenerations = numOfGenerations
        self.population = population
        self.pause = False
        print("After init EvolutionManager")
#-------------------------------------------------------------------------------------------
    def startTraining(self,event):
        """Starts training sequence"""
        x = 0
        while True:
            time.sleep(0.1) 
            while not self.pause:
#                 for x in range(0,self.numOfGenerations):
                self.population.nextGeneration()
                event.set()
                print("Iteration num ",x,"Fitness of best one is ",self.population.bestSalesman)
#             self.canvas.updateFrame(self.population.bestSalesman.dna.getAsListOfTuple())
                if x == 10:
                    self.pause = True;
                x += 1
#-------------------------------------------------------------------------------------------
    def getList(self, li):
        print(li)
        listToReturn = list()
        for x in li:
            listToReturn.append((x.tupleXY[0],x.tupleXY[1]))
        return listToReturn
#-------------------------------------------------------------------------------------------
