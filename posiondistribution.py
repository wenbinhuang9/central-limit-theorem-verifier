

import random
from  uniformdistribution import drawHist

import  numpy as np
def genPoionPopulation(lam, size):
    pop = np.random.poisson(lam, size)

    return pop
def sample(sampleNumber, population):

    pop_len = len(population)

    sampleSum = 0
    for i in range(sampleNumber):
        ran_idx = random.randrange(0, pop_len)
        sampleSum += population[ran_idx]

    return sampleSum/(sampleNumber + 0.0)

def distributionFromPoissionData(n, population):

    data = []
    for i in range(n):
        avg = sample(100, population)

        data.append(avg)

    return data

if __name__ == "__main__":
    ## this population is a normal distribution
    population= genPoionPopulation(5, 10000)

    print population
    data = distributionFromPoissionData(1000, population)

    drawHist(data)