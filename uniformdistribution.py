
# experiment of average from the most common uniform distribution.

# Define experiment of casting coins, so we have P(X = 0) = 0.5, P(X = 1) = 0.5

# sample number is 30,  and get average from the 30 sample.
import random

import matplotlib.pyplot as plt

def randomVariable():
    r = random.uniform(0, 1)
    if r <= 0.5:
        return 0
    else:
        return 1

def sampleAvg(number):
    sum = 0
    for i in range(number):
        sum += randomVariable()

    return sum/(number + 0.0)



def distribution(sampleTimes):

    avgList = []
    for i in range(sampleTimes):
        avg = sampleAvg(500)

        avgList.append(avg)
    return  avgList



def drawHist(data):
    plt.hist(data)
    plt.show()


if __name__ == "__main__":
    avgList = distribution(10000)

    drawHist(avgList)




