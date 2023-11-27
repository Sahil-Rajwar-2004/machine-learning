import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

np.random.seed(47)
X = 2 * np.random.rand(100,1)
Y = 4 + 3 * X + 1.5 * X**2 + np.random.randn(100,1)

xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size = 0.2,random_state = 47)

scaler = StandardScaler()
xtrain_scaled = scaler.fit_transform(xtrain)
xtest_scaled = scaler.transform(xtest)

alpha = 1
model = Ridge(alpha)
model.fit(xtrain_scaled,ytrain)

ypred = model.predict(xtest_scaled)

mse = mean_squared_error(ytest,ypred)
print(mse)

xrange = np.linspace(0,2,100).reshape(-1,1)
xrange_scaled = scaler.transform(xrange)
yrange_pred = model.predict(xrange_scaled)

plt.scatter(X,Y,label = "Data")
plt.plot(xrange,yrange_pred,label = f"Ridge Regression (alpha = {alpha})",color = "red")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
