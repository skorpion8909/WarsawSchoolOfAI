'''
    
    This class represents Population of DNA
    Every solution is just a list of Genoms in order
    Order determined the path: from first element of list to last element
    
    
    1.) This class manage selection(pool selection) with elitism, fitness, crossover and mutation

'''

import DNA
import Salesman
import random as r
from datetime import datetime
import time

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
    def __init__(self, populationSize, listOfPoints, mutateChance, mutateRate):
        """init list of possible Salesman paths"""
        startTime = datetime.now()
        # init variable
        self.bestSalesman = None
        # set mutate change
        self.mutateChance = mutateChance
        self.populationSize = populationSize
        # end program if starting len of list with points is less then 3
        if len(listOfPoints) <= 2:
            sys.exit("The size of list with points must be grater then ",len(listOfPoints),".");
        self.salesmanList = list()
        # determine how often mutation will happen
        self.mutateRate = mutateRate
        if int(round(self.populationSize*self.mutateRate/100)) < 1:
            self.howManyPoints = 1
        else:
            self.howManyPoints = int(round(self.populationSize*self.mutateRate/100)) 
        # if populationSize is less then 3
        if populationSize <= 3:
            print("Population size must be bigger then ",populationSize,"\n","Population size set to 10")
            self.populationSize = 10
        # create list of salesman
        for x in range(0, populationSize):
            # init new DNA and add to list
            self.salesmanList.append(Salesman.Salesman(listOfPoints))
        # round to 1.0 
        self.summedFitness = self.getSummedFitnessAndSetBestOne()
        print("New generation was done in ",(datetime.now() - startTime).total_seconds())
 #------------------------------------------------------------------------------      
    def getSummedFitnessAndSetBestOne(self):
        """ return summed fitness and sets best salesman as variable"""
        # done in one function for optimization purpose
        summ = 0
        if self.bestSalesman is None:
            self.bestSalesman = self.salesmanList[0]
        for x in self.salesmanList:
            fit = x.fitness
            summ += fit
            if fit > self.bestSalesman.fitness:
                # set new best salesman
                self.bestSalesman = x
        return summ
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

#         best half of current
#         sortedList = sorted(self.salesmanList, key=lambda x: x.distance, reverse = False)
#         nextPopulation = sortedList[:len(sortedList)*25//100]
        
        # clear the list
        self.salesmanList.clear()
        # populate with new objects
        self.salesmanList.extend(nextPopulation)
        # new generation of population a population size
        self.fillRestOfListWithSalesmenFromCrossover(nextPopulation)
        # refresh summed fitness value
        self.summedFitness = self.getSummedFitnessAndSetBestOne()
        print("New generation was done in ",(datetime.now() - startTime).total_seconds())
#------------------------------------------------------------------------------
    def getFirstPartOfNewGeneration(self):
        """
            return a list of size of 50% of salesmanList with randomly 
            choosen salesmen based on fitness probability
        """
        print(len(self.salesmanList)//2, " <--")
        stop = len(self.salesmanList)//2
        # counter for knowing when to stop a loop
        count = 3
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
            randomValue = r.uniform(0,1)
            # get next element form list
            salesman = next(iterList)
            # if rounded to 3rd decimal point probability for this salesman is grater then random value
            persentageToOthers = round((salesman.fitness*1.0/self.summedFitness)*10.0,5)
            randomValueRound = round(randomValue,5)
            if(persentageToOthers > randomValueRound):
                # this show why persentageToOthers is multiply
#             print(persentageToOthers,  randomValueRound)
                # add that element to a list that will be returned
                listToReturn.append(salesman)
                # increase var count by 1 to allowed the loop stop when we got all needed objects
                count += 1
            # if object get from iterator is the last object of that list
            if salesman is self.salesmanList[-1]:
                # refresh the iterator object
                iterList = iter(self.salesmanList)
                count += 1
        return listToReturn
#------------------------------------------------------------------------------
    def fillRestOfListWithSalesmenFromCrossover(self,nextPopulation):
        """ sets list of salesman with new generated salesmen """
        leftSpace =self.populationSize - len(nextPopulation)
        bestOnes = sorted(nextPopulation, key=lambda x: x.distance, reverse = False)
        count = 0
        for x in range(0,leftSpace//2):
#             parent1 = r.choice(bestOnes[0:len(nextPopulation)*10//100])
#             parent2 = r.choice(bestOnes[0:len(nextPopulation)*10//100])
            parent1 = r.choice(nextPopulation)
            parent2 = r.choice(nextPopulation)
            offspring1,offspring2 = self.crossoverPMX(parent1,parent2)
            self.salesmanList.append(offspring1)
            self.salesmanList.append(offspring2)
            count += 2
            if leftSpace - count == 0:
                break
        print(len(self.salesmanList) , " < sl len")
#------------------------------------------------------------------------------
    def getRandInt(self,**kwargs):
        """ returns random int in rage of list size -1"""
        if len(kwargs) == 1:
           return r.randint(0,kwargs["size"]-1)
        else:
            while True:
               ran = r.randint(0,kwargs["size"]-1)
               if ran != kwargs["used"]:
                   return ran 
#------------------------------------------------------------------------------
    def mutate(self,offspring):
        """ swaps randomly two elements of list"""
#         for x in range(0,r.randint(0,self.howManyPoints)):
        if  r.uniform(0,1) < self.mutateChance:
            position1 = self.getRandInt(size = len(offspring),)
            position2 = self.getRandInt(size = len(offspring), used = position1)
            offspring[position1] , offspring[position2] = offspring[position1], offspring[position2]
#------------------------------------------------------------------------------
    def crossoverPMX(self,parent1,parent2):
        """ returns 2 offspring(salesman object) from two 2 parents"""
        #Partially Mapped Crossover Operator
        # this fun is based on this example https://www.hindawi.com/journals/cin/2017/7430125/
        # get dna from parents
        parent2Dna = parent2.dna.chromosom
        parent1Dna = parent1.dna.chromosom

        lenght = len (parent1Dna)
        
        # prepare two list of parents len
        offspringDna1 = [0] * lenght
        offspringDna2 = [0] * lenght
      
#         if self.mutateChance > r.uniform(0,1):
#             self.mutate(parent1Dna)
#         if self.mutateChance > r.uniform(0,1):
#             self.mutate(parent2Dna)
        
        numOfPoints = len(parent1Dna)
        # -2 and after -1,  +1 makes sure that between split points there will always at least 1 value
        rsp1 = r.randint(0,numOfPoints-2) # random split point
        maxDistance = rsp1 + rsp1*5.0//100
        if maxDistance > lenght-1:
            rsp2 = lenght-1
        else:
            rsp2 = r.randint((rsp1),maxDistance) + 1 # random split point

        # stage 1 of creating offspring i passing part of parent dna defined by rsp
        offspringDna1[rsp1:rsp2] = [parent2Dna[genom] for genom in range(rsp1,rsp2)]
        offspringDna2[rsp1:rsp2] = [parent1Dna[genom] for genom in range(rsp1,rsp2)]
        
        # stage 2 is adding all genes from parent that are not in conflict
        # for len of dna
        for x in range(0,len(parent1Dna)):
            # if offspring does not contain that genom already pass it
            if not offspringDna1.__contains__(parent1Dna[x]):    
                # pass it    
                offspringDna1[x] = parent1Dna[x]
            # if offspring does not contain that genom already
            if not offspringDna2.__contains__(parent2Dna[x]): 
                # pass it     
                offspringDna2[x] = parent2Dna[x]
        # stage 3 takes care of every left spot in dna
        # if there is empty spot indicated as 0
        if offspringDna1.__contains__(0):
            # fill rest of dna
            self.fillDna(offspringDna1, parent2Dna)
       # if there is empty spot indicated as 0
        if offspringDna2.__contains__(0):
            # fill rest of dna
            self.fillDna(offspringDna2, parent1Dna)
        self.mutate(offspringDna2)
        self.mutate(offspringDna1)
        return Salesman.Salesman(offspringDna1),Salesman.Salesman(offspringDna2)
#------------------------------------------------------------------------------
    def fillDna(self, offspringDna, parentDna):
        """ returns filled dna based on second parent"""
        for x in range(len(offspringDna)):
            if 0 == offspringDna[x]:
                for y in parentDna:
                    if not offspringDna.__contains__(y):
                        offspringDna[x] = y
        return offspringDna
#------------------------------------------------------------------------------
    def crossoverMy(self,parent1,parent2):
        """ returns 2 offspring(salesman object) from two 2 parents"""
        offspringDna2 = parent2.dna.chromosom
        offspringDna1 = parent1.dna.chromosom
        mutateChance = 0.6
        self.mutate(offspringDna2,mutateChance)
        self.mutate(offspringDna1,mutateChance)
        return Salesman.Salesman(offspringDna1),Salesman.Salesman(offspringDna2)
#------------------------------------------------------------------------------    
# Tests
# Test _str
# p = Population(2500,[(0,4),(4,2),(5,2),(0,10),(4,12),(2,0),(12,8)])
# print(p)
arr = [0] * 10
bar = [3,4,5,6,7,8,0]
arr[2:4] = [bar[aa] for aa in range(2,4)]

print(arr)
