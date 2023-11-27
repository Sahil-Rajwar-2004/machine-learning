# Mean Squared Error

def mse(yTrue,yPred):
    total = 0
    length = len(yTrue)
    for i in range(length):
        total += (yTrue[i] - yPred[i])**2
    return total / length

x = [1,2,3,4,5]
y = [0,2,3.5,5,4.89]

print(mse(x,y))

