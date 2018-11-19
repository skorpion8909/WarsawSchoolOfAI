
"""
    ******************************************************************
    *                                                                *
    * Travel Sales Man problem is a type of problem where we can use *
    * genethic algorithm to find better ans faster answear.          *
    *                                                                *
    ******************************************************************
    
    1.) This class is main class for this procjet

"""
import Population
import EvolutionManager

def main():
    # list o points
    listOfCities = [(0,12),(12,5),(14,20),(45,5),(14,53),(1,8)]
    
    #initalize list of paths
    population = Population.Population(20,listOfCities)
#     bestOne = Population.



if __name__ == '__main__':
    main()