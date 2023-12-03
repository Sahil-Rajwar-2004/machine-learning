import numpy as np

class LogisticRegression:
    def __init__(self,learning_rate = 0.01,epochs = 1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None

    def sigmoid(self,z):
        return 1/(1 + np.exp(-z))

    def fit(self,xTrain,yTrain):
        self.weights = np.zeros(xTrain.shape[1])
        # print(self.weights)
        for _ in range(self.epochs):
            z = np.dot(xTrain,self.weights)
            predictions = self.sigmoid(z)
            gradient = np.dot(xTrain.T,(predictions - yTrain)) / len(yTrain)
            self.weights -= self.learning_rate * gradient
        # return self.weights,xTrain.shape[1]

    def predict(self,xTest):
        predictions = self.sigmoid(np.dot(xTest,self.weights))
        return np.round(predictions)

xTrain = np.array([[1,2],[2,3],[3,4]])
yTrain = np.array([0,0,1])

model = LogisticRegression()
model.fit(xTrain,yTrain)

xTest = np.array([[1,1],[2,2]])
predictions = model.predict(xTest)

print(predictions)
