# Mean Absolute Error

def mae(yTrue,yPred): 
    total = 0
    length = len(yTrue)
    for i in range(length):
        total += abs(yTrue[i] - yPred[i])
    return total / length

x = [1,2,3,4,5]
y = [0,2,3.5,5,4.89]

print(mae(x,y))
