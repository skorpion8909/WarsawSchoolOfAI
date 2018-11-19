"""
    This class represent a Salesman object 
    The path is determined by his DNA

"""
import DNA
import random as r

class Salesman:
#---------------------------------------------------------------------------
    def __init__(self,listOfPoints):
        x = r.sample(listOfPoints, len(listOfPoints))
        self.dna = DNA.Dna(x)
#---------------------------------------------------------------------------
    def setDnaList(self,list):
        self.dna.setDnaList(list)
#---------------------------------------------------------------------------
    def __str__(self):
        return str(self.dna)
#---------------------------------------------------------------------------
#TEST