if __name__ == "__main__":
    import pyperclip
import random as r
import math as m
#--------------------------------------------------------------------------------
def di(p1,p2):
    """ returns distance between points"""
    return (m.sqrt(m.pow(p1[0] - p2[0],2)) + m.pow((p1[1] - p2[1]),2))
#--------------------------------------------------------------------------------
def genRandomListOfPoints(sizeOfList,height,width):
    """ returns list with random points in range of window as tuple"""
    listToReturn = list()
    minimumDistance = 5
    he = height - 10
    wi = width - 10
    notValidPoint = True
    distanceIsCorrect = False
    while len(listToReturn) < sizeOfList:
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
    if __name__ == "__main__":    
        # add to clipboard
        pyperclip.copy(str(listToReturn))
    return listToReturn
#--------------------------------------------------------------------------------
