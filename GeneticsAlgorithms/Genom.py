""" 
    
    This class represents one Genom of DNA
    Genom in this case is just pair of values x and y 
    that represents a point which is single city.
    

"""

class Genom(object):
#------------------------------------------------------------------------------------------------
    def __init__(self,tuple):  #gest a tuple of x and y
        # init of genom
        self.x = tuple[0]
        self.y = tuple[1]
#------------------------------------------------------------------------------------------------
    def __str__(self):
        return "(%s, %s)" %(self.x,self.y)
#------------------------------------------------------------------------------------------------
#Test
#print(Genom(0,4))