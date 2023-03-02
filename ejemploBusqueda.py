import random

def buildListOfRandomNumber(N, inferiorRange, superiorRange):
    listOfRandomNumbers = []
    for randomNumber in range(0,N):
        listOfRandomNumbers.append(random.randint(inferiorRange,superiorRange))
    return listOfRandomNumbers

#buscar si un numero X está en la lista de aleatorios
#En caso de que el numero esté devolver la posición del numero

def searchNumberInRandomList(numberToFind,listToSearch):
    found = False
    for index, element in enumerate(listToSearch):
        if element == numberToFind:
            return index
    return found


randomList = buildListOfRandomNumber(50, 0, 100)
found = searchNumberInRandomList(16, randomList)
print(randomList)
print(found)
