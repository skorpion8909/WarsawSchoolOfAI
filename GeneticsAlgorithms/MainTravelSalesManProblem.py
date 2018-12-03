
"""
    ******************************************************************
    *                                                                *
    * Travel Sales Man problem is a type of problem where we can use *
    * genethic algorithm to find better ans faster answear.          *
    *                                                                *
    ******************************************************************
    
    1.) This class is main class for this project

"""
import Population
import EvolutionManager
import random as r
import math as m

def di(p1,p2):
    return (m.sqrt(m.pow(p1[0] - p2[0],2)) + m.pow((p1[1] - p2[1]),2))

def genRandomListOfPoints(sizeOfList,height,width):
    """ returns list with random points in range of window as tuple"""
    listToReturn = list()
    minimumDistance = 5
    he = height - 10
    wi = width - 10
    notValidPoint = True
    distanceIsCorrect = False
    while len(listToReturn) < 10:
        while notValidPoint:
            randomPoint = (r.randint(10,he),r.randint(10,wi))
            if len(listToReturn) == 0:
                listToReturn.append(randomPoint)
                break
            for p in listToReturn:
                if di(randomPoint,p) >= 5:
                    distanceIsCorrect = True
                else:
                    distanceIsCorrect = False
            if distanceIsCorrect:
                listToReturn.append(randomPoint)
                break
        print(len(listToReturn))
    return listToReturn
#-------------------------------------------------------------------------------------
def main():
    # list o points
    height = 400
    width = 800
    print("Lol")
    print(genRandomListOfPoints(5,height,width))
#     listOfCities = [(0,12),(12,5),(14,20),(45,5),(14,53),(1,8)]
    
    #initalize list of paths
#     population = Population.Population(50,listOfCities)
#     population.nextGeneration()
#   bestOne = Population.
#-------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------------
