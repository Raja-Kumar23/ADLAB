# 19. Compare Gaussian NB vs Logistic Regression on the same dataset and analyze results
import math
X = [1,2,3,4,5,6,7,8]
y = [0,0,0,0,1,1,1,1]
class0 = [X[i] for i in range(len(X)) if y[i] == 0]
class1 = [X[i] for i in range(len(X)) if y[i] == 1]
mean0 = sum(class0) / len(class0)
mean1 = sum(class1) / len(class1)
var0 = sum((x - mean0)**2 for x in class0) / len(class0)
var1 = sum((x - mean1)**2 for x in class1) / len(class1)
prior0 = len(class0) / len(X)
prior1 = len(class1) / len(X)
def gaussian(x, m, v):
    return (1 / math.sqrt(2 * math.pi * v)) * math.exp(-(x - m)**2 / (2 * v))
test = 4.5
p0 = prior0 * gaussian(test, mean0, var0)
p1 = prior1 * gaussian(test, mean1, var1)
nb_prediction = 0 if p0 > p1 else 1
w = 0.5
b = -3
def sigmoid(z):
    return 1 / (1 + math.exp(-z))
z = w * test + b
prob = sigmoid(z)
lr_prediction = 1 if prob >= 0.5 else 0
print("Test Value:", test)
print("Gaussian NB Prediction:", nb_prediction)
print("Logistic Regression Prediction:", lr_prediction)
print("Raja Kumar Sah, 23053769")
