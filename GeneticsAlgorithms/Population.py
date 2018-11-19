'''
    
    This class represents Population of DNA
    Every solution is just a list of Genoms in order
    Order determined the path: from first element of list to last element
    
    
    1.) This class manage selection, fitness and crossover fun

'''

import DNA
import Salesman
from itertools import cycle
import math as m

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
    licycle = cycle(listOfPoint)
    # Prime the pump
    p2 = next(licycle)
    while running:
        p1, p2 = p2, next(licycle)
        distance = 0
        distance += distanceBetweenPoints(p1,p2) 
        if p2 == listOfPoint[-1]:
            running = False
    return distance
#------------------------------------------------------------------------------
class Population:
    def __init__(self,populationSize,listOfPoints):
        # init list of possible Salesman paths
        self.list = list()
        for x in range(0, populationSize):
            self.list.append(Salesman.Salesman(listOfPoints)) # init new DNA and add to list
 #------------------------------------------------------------------------------           
    def __str__(self):
        listToJoin = list()
        for x in self.list:
            listToJoin.append(str(x))
        stringToReturn = '\n'.join(listToJoin)
        stringToReturn +="\n"
        return stringToReturn
#------------------------------------------------------------------------------
    def countFitnesForPopulation(self):
        dictOfFitness = dict() # key is fitnes score, value is Salesman object
        for x in self.list:
            fitness = countFitnes(x)
            if fitness in dictOfFitness:
                dictOfFitness[fitness].append(x)
            else:
                dictOfFitness[fitness] = [x]
        print(len(dictOfFitness))
        return dictOfFitness
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
