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
        return m.pow((1.0/self.distance),2)
#         return (1.0/self.distance)
#TEST
