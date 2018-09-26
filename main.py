import random, string, time
from bitarray import bitarray

def targetString():
    return "Hello World!"

def populationSize():
    return 1000000

def main():
    start = time.time()
    population = generatePopulation(populationSize())
    for str in population:
        value = fitness(str, targetString())
        if value < 9:
            print (value, str)
    end = time.time()
    print(crossover(0))
    print("{}{}{}".format("The process took ", end - start, " seconds"))

def generatePopulation(size):
    population = []
    for i in range(0,size):
        chromosome = []
        for char in range(0,len(targetString())):
            char = random.choice(string.printable)
            chromosome.append(char)
        chromoString = ''.join(chromosome)
        population.append(chromoString)
    return population

def fitness(source, target):
    if len(source) == len(target):
        pairs = zip(source, target)
        hammingDistance = 0
        for a, b in pairs:
            if a != b:
                hammingDistance += 1
        return hammingDistance

def crossover(chromosome):
    bitArray = bitarray(2**2)
    return bitArray

"""def checkSimilarity(population targetString):
    targetString = [Hello World!]
    for chr in population:
"""

if __name__ == "__main__":
    main()
