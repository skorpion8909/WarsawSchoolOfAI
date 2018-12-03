import random as r
import Genom

'''
    This class represents represents possible solution as DNA
    DNA(one chromosom) is implemented as a list of genoms
        
'''

class Dna:
#------------------------------------------------------------------------------------------------------------- 
    def __init__(self,listOfPoints):
        #on init generates a chromosom of genoms from chromosom of points
        self.chromosom = self.makeListOfGenoms(listOfPoints)
#------------------------------------------------------------------------------------------------------------- 
    # set new DNA
    def makeListOfGenoms(self,listOfPoints):
        # return chromosom of genoms
        listToReturn = list()
        for point in listOfPoints:
            listToReturn.append(Genom.Genom(point))
    
        return listToReturn
#-------------------------------------------------------------------------------------------------------------         
    # takes listOfGenoms as replace for current 
    def setDnaList(self,listOfGenoms): 
        self.chromosom = list
#-------------------------------------------------------------------------------------------------------------         
    def __str__(self):
        return "This DNA has\nThe first point as %s\nThe last point as %s" % (self.chromosom[0],self.chromosom[-1])
#------------------------------------------------------------------------------------------------------------- 
    def __eq__(self, other):
        """class override equels method"""
        if isinstance(other, self.__class__):
            if self.chromosom == other.chromosom:
                return True
        else:
            return False
#------------------------------------------------------------------------------------------------------------- 
    def getAsListOfTuple(self):
        """ returns chromosom as a list of tuple"""
        listToReturn = list()
        for x in self.chromosom:
            listToReturn.append((x.tupleXY[0],x.tupleXY[1]))
        return listToReturn
#-------------------------------------------------------------------------------------------------------------             
# Test
# dna = Dna([(0,5),(4,1),(44,55),(2,44)])
# print(dna)    
# for x in dna.chromosom:
#    print(x)
