""" 
    
    This class represents one Genom of DNA
    Genom in this case is just pair of values x and y 
    that represents a point which is single city.
    

"""

class Genom:
#------------------------------------------------------------------------------------------------
    def __init__(self,tuple):  #gest a tuple of x and y
        # init of genom
        self.tupleXY = tuple
#------------------------------------------------------------------------------------------------
    def __str__(self):
        return "(%s, %s)" %(self.tupleXY[0],self.tupleXY[1])
#------------------------------------------------------------------------------------------------
    def __eq__(self, other):
       """class override equels method"""
       if isinstance(other, self.__class__):
           if self.tupleXY[0] == other.tupleXY[0] and self.tupleXY[1] == other.tupleXY[1]:
               return True
       else:
           return False
#------------------------------------------------------------------------------------------------        
#Test
# print(Genom((0,4)))