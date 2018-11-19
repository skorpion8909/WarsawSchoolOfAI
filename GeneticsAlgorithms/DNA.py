import random as r
import Genom

'''
    This class represents represents possible solution as DNA
    DNA is a list of genoms
        
'''

class Dna:
#------------------------------------------------------------------------------------------------------------- 
    def __init__(self,list):
        #on init generates a list of genoms from list of points
        self.list = self.makeListOfGenoms(list)
#------------------------------------------------------------------------------------------------------------- 
    # set new DNA
    def makeListOfGenoms(self,listOfPoints):
        # return list of genoms
        listToReturn = list()
        for point in listOfPoints:
            listToReturn.append(Genom.Genom(point))
    
        return listToReturn
#-------------------------------------------------------------------------------------------------------------         
    # takes listOfGenoms as replace for current 
    def setDnaList(self,listOfGenoms): 
        self.list = list
#-------------------------------------------------------------------------------------------------------------         
    def __str__(self):
        return "This DNA has\nThe first point as %s\nThe last point as %s" % (self.list[0],self.list[-1])
#------------------------------------------------------------------------------------------------------------- 
    def __eq__(self, other):
        """class override equels method"""
        if isinstance(other, self.__class__):
            if self.list == other.list:
                return True
        else:
            return False
#-------------------------------------------------------------------------------------------------------------             
# Test
# dna = Dna([(0,5),(4,1),(44,55),(2,44)])
# print(dna)    
# for x in dna.list:
#    print(x)
