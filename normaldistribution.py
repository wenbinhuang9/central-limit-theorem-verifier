# how to mock the normal distribution here??? we can use avg distribution from uniform distribution

import  random

from  uniformdistribution import distribution, drawHist

def sample(sampleNumber, population):

    pop_len = len(population)

    sampleSum = 0
    for i in range(sampleNumber):
        ran_idx = random.randrange(0, pop_len)
        sampleSum += population[ran_idx]

    return sampleSum/(sampleNumber + 0.0)


def distributionFromNormalData(n, population):

    data = []
    for i in range(n):
        avg = sample(100, population)

        data.append(avg)

    return data

if __name__ == "__main__":
    ## this population is a normal distribution
    population= distribution(3000)

    data = distributionFromNormalData(100, population)

    drawHist(data)





