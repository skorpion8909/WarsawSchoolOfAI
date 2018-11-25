"""
    
    This class governs process of looking for better
    combination making a path for a traveler
    

"""
import Population

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
            print("Iteration num ",x,"Fitness of best one is ",self.population.bestSalesman)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------

# Test
listOfCities = [(0,12),(12,5),(14,20),(45,5),(14,53),(1,8),(22,11),(10,84),(90,23)]
    
#initalize list of paths
population = Population.Population(50,listOfCities)
population.nextGeneration()
EM = EvolutionManager(20000,population)
EM.startTraining()
