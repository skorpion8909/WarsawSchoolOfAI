"""
    This class represent a Salesman object 
    The path is determined by his DNA
    
    1.) fitness is performance of path
    2.) dna is the path
    
"""
import DNA
import random as r
from itertools import cycle
import math as m

#------------------------------------------------------------------------------
def distanceBetweenPoints(firstGenom,secoundGenom):
    """Counts distance between two points"""
    
    p1 = firstGenom.tupleXY    # get tuple from Genom Object 1
    p2 = secoundGenom.tupleXY  # get tuple from Genom Object 2
   
    # returns simple = sqrt((x1 - x2)**2 + (y1,y2)**2)
    return m.sqrt(m.pow(p1[0] - p2[0],2) + m.pow(p1[1] - p2[1],2))
#------------------------------------------------------------------------------
class Salesman:
#---------------------------------------------------------------------------
    def __init__(self,listOfPoints):
        x = r.sample(listOfPoints, len(listOfPoints))
        self.dna = DNA.Dna(x)
        self.distance = self.countDistance()
        self.fitness = self.countFitness()              
#---------------------------------------------------------------------------
    def setDnaList(self,list):
        self.dna.setDnaList(list)
        self.distance = self.countDistance()
        self.fitness = self.countFitness()
#---------------------------------------------------------------------------
    def __str__(self):
        return str("Fitness is " + str(self.fitness) +" "+ str(self.dna))
#---------------------------------------------------------------------------
    def __eq__(self, other):
        """class override equels method"""
        if type(self) == type(other):
            if self.dna == other.dna:
                 return True
            else:
                return False
        else:
            return False
#------------------------------------------------------------------------------
    def countDistance(self):
        """Count distance for this Salesman"""
        listOfPoint = self.dna.chromosom
        running = True
        listCycle = cycle(listOfPoint)                  # this lets to take 2 elements of list every one step of loop
        # Prime the pump
        p2 = next(listCycle)                            # set the p2 a first element of list
        distance = 0
        while running:
            p1, p2 = p2, next(listCycle)                # set p2 is na p1 and p2 is new next element from list
            distance += distanceBetweenPoints(p1,p2)    # count distance between points and sums it
            if p2 == listOfPoint[-1]:
                distance += distanceBetweenPoints(p2,listOfPoint[0])                   # if p2 as the same as last point it means list is empty
                running = False                         # prevent next loop cycle
        return distance
#---------------------------------------------------------------------------
    def countFitness(self):
        """Count fitness for this Salesman"""
#         return m.sqrt((1.0/self.distance))
        return m.pow((1.0/(self.distance*1.0)),2)
#         return (1.0/self.distance)
#TEST
# from Population import Population
# class Manager():    
#      def __init__(self):
#          """ create next generation of creatures"""
#          # init first population pool
#          self.population = Population.loadRandomPopulation()
#          self.population.evaluate # prepare for next step 
# #...
# #in Creature class ...
# class Population():
# #...
#     def evaluate(self):
#         """ update objects"""
#         for creature in self.populationPool:
#             creature.countFitness() 
#         self.countSummedFitness()
#         self.countChanceForAll() 
# #-----------------------------------------------------------------------------------
#     def countChanceForAll(self):
#         """ count chance """
#         # for pool selection
#         for creature in self.populationPool:
#             creature.countChance()                    
#                                                # working correctly if sum of all
#                                                # creatures fitness in population
#                                                # is equal to 1    
# #in Creature class .
# from DNA import DNA
# class Creature():
#     def __init__(self,manager):
#         """ create next generation of creatures"""
#         self.manager = manager
#         self.creatureDNA = DNA.DNA(self.manager)
#         # fields...
# #-----------------------------------------------------------------------------------
#     def countFitness(self):
#         """ return counted fitness for"""
#         return self.creatureDNA.getFitness() # manager makes all operation
# #-----------------------------------------------------------------------------------
#     def countChance(self):
#         """ return counted fitness for"""
#         return  self.fitness/self.manager.summedFitness  # manager makes all operation
# #-----------------------------------------------------------------------------------
# #...
#  
#  
#  
# from itertools import cycle
# import random as r
# #-------------------------------------------------------------------------------------------  
# #...
#...
# def selectFromPopulationToCrossover(self):
#     """ return list of objects chosen to crossover"""
#     currentPopulationList = self.getCurrentPopulation()
#   
#     # pool selection
#     listToReturn = list()
#     stopCounter = 0 
#     iterator = cycle(currentPopulationList)
#     while True:
#         creature = next(iterator)
#         randValue = r.uniform(0,1) # return float value between 0 and 1
#         if creature.chance > randValue:
#             listToReturn.append(creature)
#             stopCounter += 1
#             # stop when 
#             if stopCounter == len(currentPopulationList)//2:
#                 break
#         # refresh iteration pool
#         if creature == currentPopulationList[-1]:
#             iterator = cycle(currentPopulationList)
#     #end of loop=        
#     # another way for a selection
#     # sortedList = sorted(currentPopulationList, key=lambda x: x.fitness, reverse = False)
#     # listToReturn = sortedList(:len(sortedList)*50.0//100)
#     # return listToReturn
#   
#     return listToReturn
# #-------------------------------------------------------------------------------------------     
# #...
# #  
# #  
# # #...
# # #------------------------------------------------------------------------------------------- 
# #  
# 
# 
# #-------------------------------------------------------------------------------------------  
# def selectAndCrossover(self):
#     """ return list of objects chosen to crossover"""
#     currentPopulationList = self.currentPopulation
#     # pool selection
#     listToReturn = list()
#     stopCounter = 0 
#     iterator = cycle(currentPopulationList)
#     parent1 = None
#     parent2 = None
#     while True:
#         creature = next(iterator)
#         randValue = r.uniform(0,1) # return float value between 0 and 1
#         if creature.chance > randValue:
#             parent2, parent1 = parent1, creature
#             if parent2 != None:
#                 # creating new organism
#                 offspring1, offspring2 = self.crossoverPMX(parent1,parent2)
#                 listToReturn.append(offspring1)
#                 listToReturn.append(offspring2)
#                 stopCounter += 2
#                 # stop criteria
#                 if stopCounter == len(currentPopulationList)//2:
#                     break
#                 # reset parents
#                 parent1, parent2 = None, None
#         # refresh iteration pool
#         if creature == currentPopulationList[-1]:
#             iterator = cycle(currentPopulationList)
#     # set new population
#     self.currentPopulation = listToReturn
# #-------------------------------------------------------------------------------------------  
#   
#  
#  
#  
#  
# 
# 
# 
# 
# 
# 
# 


