'''
    
    This class represents Population of DNA
    Every solution is just a list of Genoms in order
    Order determined the path: from first element of list to last element
    
    
    1.) This class manage selection, fitness and crossover fun

'''

import DNA
import Salesman

class Population(object):
#------------------------------------------------------------------------------
    def __init__(self,populationSize,listOfPoints):
        # init list of possible Salesman paths
        self.list = list()
        for x in range(0, populationSize):
            self.list.append(Salesman.Salesman(listOfPoints)) # init new DNA and add to list
            
    def __str__(self):
        listToJoin = list()
        for x in self.list:
            listToJoin.append(str(x))
        stringToReturn = '\n'.join(listToJoin)
        stringToReturn +="\n"
        return stringToReturn
#------------------------------------------------------------------------------            
#Test
# print(Population(2,[(0,4),(4,2)]))
    
    