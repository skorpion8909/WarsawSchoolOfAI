'''
    
    This class represents Population of DNA
    Every solution is just a list of Genoms in order
    Order determined the path: from first element of list to last element
    
    
    1.) This class manage selection(pool selection), fitness and crossover
    2.) Does not store the same salesman objects while counting fitness

'''

import DNA
import Salesman
from itertools import cycle
import math as m
#------------------------------------------------------------------------------
def doesNotHaveTheSameDNA(salesman,listOfSalesmen):
    """checks if objects from list dont have the same DNA"""
    returnValue = True
    for man in listOfSalesmen:
        if man == salesman:
            returnValue = False
    return returnValue
#------------------------------------------------------------------------------
def distanceBetweenPoints(firstGenom,secoundGenom):
    """Counts distance between two points"""
    
    p1 = firstGenom.tupleXY    # get tuples form Genom Object 1
    p2 = secoundGenom.tupleXY  # get tuples form Genom Object 2
   
    # returns simple = sqrt((x1 - x2)**2 + (y1,y2)**2)
    return (m.sqrt(m.pow(p1[0] - p2[0],2)) + m.pow((p1[1] - p2[1]),2))
#------------------------------------------------------------------------------
def countFitnes(salesman):
    """Count fitness for this Salesman"""
    listOfPoint = salesman.dna.list
    running = True
    listCycle = cycle(listOfPoint)                  # this lets to take 2 elements of list every one step of loop
    # Prime the pump
    p2 = next(listCycle)                            # set the p2 a first element of list
    while running:
        p1, p2 = p2, next(listCycle)                # set p2 is na p1 and p2 is new next element from list
        distance = 0
        distance += distanceBetweenPoints(p1,p2)    # count distance between points and sums it
        if p2 == listOfPoint[-1]:                   # if p2 as the same as last point it means list is empty
            running = False                         # prevent next loop cycle
    return distance
#------------------------------------------------------------------------------
class Population:
    def __init__(self,populationSize,listOfPoints):
        """init list of possible Salesman paths"""
        self.list = list()
        for x in range(0, populationSize):
            self.list.append(Salesman.Salesman(listOfPoints)) # init new DNA and add to list
 #------------------------------------------------------------------------------           
    def __str__(self):
        """standard python fun for displaying class info"""
        listToJoin = list()
        for x in self.list:
            listToJoin.append(str(x))
        stringToReturn = '\n'.join(listToJoin)
        stringToReturn +="\n"
        return stringToReturn
#------------------------------------------------------------------------------
    def countFitnesForPopulation(self):
        """counts fitness for all Salesman and return dict{fitness:Salesman}"""
        dictOfFitness = dict() # key is fitness score, value is list of  Salesman objects
        for x in self.list:
            fitness = 1.0/countFitnes(x)
            if fitness in dictOfFitness:
                #check if object does not have the same DNA as those stored in the list
                if(doesNotHaveTheSameDNA(x,dictOfFitness[fitness])):
                    dictOfFitness[fitness].append(x)   # key is a 1/fitness because the best path will be the shortest 
            else:                                            # so for future pool selection perpouse 1/3 is bigger then 1/9
                dictOfFitness[fitness] = [x]
        return dictOfFitness
#------------------------------------------------------------------------------
    def nextGeneration(self):
        """generates next generation of population"""
        dict = self.countFitnesForPopulation()       #get dict for this population
#         for key,value in dict.items():
#             
#------------------------------------------------------------------------------
# Tests
# Test _str
# p = Population(1000,[(0,4),(4,2),(5,2),(0,10),(4,12),(2,0),(12,8)])
# print(p)
# Test countFitnes(x)
# dict = p.countFitnesForPopulation()    
# for x,y in dict.items():
#     print(x)
#     for yy in y:
#         print(y)
