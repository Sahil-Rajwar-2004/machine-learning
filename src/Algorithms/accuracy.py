# Accuracy Score

def accuracy_score(yTrue,yPred,tolerance = 0):
    correct_predictions = sum(1 for true,pred in zip(yTrue,yPred) if abs(true - pred) <= tolerance)
    total_samples = len(yTrue)
    accuracy = correct_predictions / total_samples
    return accuracy

x = [1, 0, 1, 1, 0, 1, 0, 1]
y = [1, 0, 1, 0, 0, 1, 1, 1]

print(accuracy_score(x,y,1))
