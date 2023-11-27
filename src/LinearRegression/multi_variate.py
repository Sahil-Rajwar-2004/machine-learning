import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

np.random.seed(47)
X1 = 2 * np.random.rand(100,1)
X2 = 3 * np.random.randn(100,1)
Y = 4 + 3 * X1 + 2 * X2+ np.random.randn(100,1)

X = np.concatenate((X1,X2),axis = 1)

xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size = 0.2,random_state = 47)

model = LinearRegression()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)

fig = plt.figure(figsize = (12,6))
ax = fig.add_subplot(111,projection = '3d')

ax.scatter(xtest[:, 0],xtest[:, 1],ytest,color = 'red',label = 'Actual Values')
ax.scatter(xtest[:, 0],xtest[:, 1],ypred,color = 'blue', label = 'Predicted Values')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')
ax.set_title('Actual vs Predicted Values')

ax.legend()
plt.show()

print(mean_squared_error(ytest,ypred))
print(model.coef_)
print(model.intercept_)
