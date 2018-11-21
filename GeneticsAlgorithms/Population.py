'''
    
    This class represents Population of DNA
    Every solution is just a list of Genoms in order
    Order determined the path: from first element of list to last element
    
    
    1.) This class manage selection(pool selection), fitness, crossover and elitism

'''

import DNA
import Salesman
import random as r
from tensorflow.python.framework.test_ops import none
from datetime import datetime

#------------------------------------------------------------------------------
def poolSelection(fitnessDict):
    """
        make a list where the best salesmann is most probably and
        the worst most likly to be pick
    """
    listOfSalesman = list()
    fitnessSum = getSummedFitness(dict)
    for key,value in fitnessDict.items():
        pass
#------------------------------------------------------------------------------
def doesNotHaveTheSameDNA(salesman,listOfSalesmen):
    """checks if objects from list dont have the same DNA"""
    returnValue = True
    for man in listOfSalesmen:
        if man == salesman:
            returnValue = False
    return returnValue
#------------------------------------------------------------------------------
class Population:
    def __init__(self,populationSize,listOfPoints):
        """init list of possible Salesman paths"""
        # end program if starting len of list with points is less then 3
        if len(listOfPoints) <= 2:
            sys.exit("The size of list with points must be grater then ",len(listOfPoints),".");
        self.salesmanList = list()
        # determine how often mutation will happen
        self.mutationRate = 0.05
        # if populationSize is less then 3
        if populationSize <= 3:
            print("Population size must be bigger then ",populationSize,"\n","Population size set to 10")
            populationSize = 10
        # create list of salesman
        for x in range(0, populationSize):
            # init new DNA and add to list
            self.salesmanList.append(Salesman.Salesman(listOfPoints)) 
        self.summedFitness = self.getSummedFitness()
 #------------------------------------------------------------------------------      
    def getSummedFitness(self):
        sum = 0
        for x in self.salesmanList:
            sum += x.fitness
        return sum
#------------------------------------------------------------------------------
    def __str__(self):
        """standard python fun for displaying class info"""
        listToJoin = list()
        for x in self.salesmanList:
            listToJoin.append(str(x))
        stringToReturn = '\n'.join(listToJoin)
        stringToReturn +="\n"
        return stringToReturn
#------------------------------------------------------------------------------
    def nextGeneration(self):
        """generates next generation of population"""
        startTime = datetime.now()
        # Next generation contains 50% salesman from old one
        # of best solution from previous generation and rest generated by crossover
        # choose randomly 50% of next population
        nextPopulation = self.getFirstPartOfNewGeneration()
        # new generation of population
        self.salesmanList = self.fillRestOfListWithSalesmenFromCrossover(nextPopulation)
        print("New generation was done in ",(datetime.now() - startTime).total_seconds())
#------------------------------------------------------------------------------
    def getFirstPartOfNewGeneration(self):
        """
            return a list of size of 50% of salesmanList with randomly 
            choosen salesmen based on fitness probability
        """
        stop = len(self.salesmanList)*0.50 - 3
        # counter for knowing when to stop a loop
        count = 0
        # we create this object to iter over it
        iterList = iter(self.salesmanList)
        # elitism
        # first we make sure that 3 of current best solution will be in next gen
        elitismList = sorted(self.salesmanList, key=lambda x: x.fitness, reverse = True)
        # first 3 elements will be the best one from last population
        listToReturn = list(elitismList[0:3])
        # as long as count did not reach 50% of len of population size
        while count < stop:
            # choose a random value between 0 and 1
            randomValue = r.uniform(0,1.0)
            # get next element form list
            salesman = next(iterList)
            # if rounded to 3 decimal point probability for this salesman is grater then random value
            if(round(salesman.fitness*1.0/self.summedFitness*1.0,3) > randomValue):
                # add that elemento to list that will be returned
                listToReturn.append(salesman)
                # increase var count by 1 to allowed the loop stop when we got all needed objects
                count += 1
            # if object get from iterator is the last object of that list
            if salesman is self.salesmanList[-1]:
                # refresh the iterator object
                iterList = iter(self.salesmanList)
        return listToReturn
#------------------------------------------------------------------------------
    def fillRestOfListWithSalesmenFromCrossover(self,nextPopulation):
        """ returns list of salesman fill from crossover """
        leftSpace = len(self.salesmanList) - len(nextPopulation)
        listToReturn = list(nextPopulation)
        for x in range(0,leftSpace):
            parent1 = r.choice(nextPopulation)
            parent2 = r.choice(nextPopulation)
            offspring = self.crossover(parent1,parent2)
            listToReturn.append(offspring)
        return listToReturn
#------------------------------------------------------------------------------
    def crossoverCX2(self,parent1,parent2):
        # this fun is based on this example https://www.hindawi.com/journals/cin/2017/7430125/
        """ returns new salesman object made of 2 parents"""
        # parents are equal in lenght
        numOfPoints = len(parent1.dna.chromosom)-1  # -1 because counting of list starts from 0 not 1
        # make sure that p1 is the best of parents
#         if parent1.fitness > parent2.fitness:
#             p1 = parent1
#             p2 = parent2
#         else:
#             p1 = parent2
#             p2 = parent1
        # let's choose 1 by that we decide that new one will be never a copy of a parent
        rsp = r.randint(1,numOfPoints) # random split point
        listForNewSalesman = list(parent1.dna.chromosom[0:rsp])
        listForNewSalesman.extend(parent2.dna.chromosom[rsp:])
        return Salesman.Salesman(listForNewSalesman)
# Tests
# Test _str
p = Population(2750,[(0,4),(4,2),(5,2),(0,10),(4,12),(2,0),(12,8)])
# print(p)
# Test countFitnes(x)
# dict = p.countFitnesForPopulation()    
# for x,y in dict.items():
#     print(x)
#     for yy in y:
#         print(y)
p.nextGeneration()
lista = [0,1,2,3,4]
listb = [5,6,7,8,9]
listc = lista[0:1]
listc.extend(listb[1:])
print(listc)




