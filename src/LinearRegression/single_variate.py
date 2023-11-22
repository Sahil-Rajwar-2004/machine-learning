import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

np.random.seed(47)
X = 2 * np.random.rand(100,1)
Y = 4 + 3 * X + np.random.randn(100,1)

xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size = 0.2,random_state = 47)

model = LinearRegression()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)

plt.scatter(xtrain,ytrain,color = "blue",label = "Training Data")
plt.scatter(xtest,ytest,color = "red",label = "Test Data")
plt.plot(xtest,ypred,color = "green",linewidth = 3,label = "Regression Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
