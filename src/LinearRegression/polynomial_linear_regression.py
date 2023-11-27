import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

np.random.seed(47)
X = 2 * np.random.rand(100,1)
Y = 3 * X + 0.5 * X**2 + np.random.randn(100,1)

degree = 3
model = make_pipeline(PolynomialFeatures(degree),LinearRegression())
model.fit(X,Y)

plotX = np.linspace(0, 2, 100).reshape(-1, 1)
plotY = model.predict(plotX)

plt.scatter(X,Y,label = 'Data')
plt.plot(plotX,plotY,label = f'Polynomial Regression (Degree {degree})',color = 'red')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
