# Fit Transform

from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1,2],[2,3],[3,4]])

scaler = StandardScaler()

def custom_fit_transform(X):
    mean = np.mean(X,axis = 0)
    std = np.std(X,axis = 0)
    X_transformed = (X - mean) / std
    return X_transformed

print(scaler.fit_transform(X))
print(custom_fit_transform(X))
