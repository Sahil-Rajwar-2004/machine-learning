# Single-Variate Linear Regression

import numpy as np
import matplotlib.pyplot as plt

def linear_regression(x,y):
    x = np.array(x)
    y = np.array(y)
    meanX = np.mean(x)
    meanY = np.mean(y)
    slope = np.sum((x - meanX) * (y - meanY)) / np.sum((x - meanX) ** 2)
    intercept = meanY - slope * meanX
    return (slope,intercept)

def plot_regression_line(x,y,slope,intercept):
    plt.scatter(x,y,color = 'blue',label = 'Data Points')
    plt.plot(x,slope * x + intercept,color = 'red',label = 'Regression Line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression')
    plt.legend()
    plt.grid(True)
    plt.show()

x = np.array([1,2,3,4,5])
y = np.array([2,4,5,4,5])

slope,intercept = linear_regression(x,y)
print(slope,intercept)
plot_regression_line(x,y,slope,intercept)
