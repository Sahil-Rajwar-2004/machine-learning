# Root Mean Squared Error

import math

def rmse(yTest,yPred):
    total = 0
    length = len(yTest)
    for i in range(length):
        total += (yTest[i] - yPred[i])**2
    return math.sqrt(total / length)

x = [1,2,3,4,5]
y = [0,2,3.5,5,4.89]

print(rmse(x,y))
