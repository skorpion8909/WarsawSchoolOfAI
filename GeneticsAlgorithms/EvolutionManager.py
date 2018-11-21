"""
    
    This class governs process of looking for better
    combination making a path for a traveler
    

"""


#-------------------------------------------------------------------------------------------
class EvolutionManager:
    def __init__(self, numOfGenerations,population):
        """Takes number of generations and Population() object"""
        self.numOfGenerations = numOfGenerations
        self.population = population
#-------------------------------------------------------------------------------------------
    def startTraining(self):
        """Starts training sequence"""
        for x in range(0,self.numOfGenerations):
            self.population.nextGeneration()
            print("Iteration num ",x,population)
#-------------------------------------------------------------------------------------------
#     def 
#-------------------------------------------------------------------------------------------
