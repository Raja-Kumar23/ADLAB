# 10. Implement train-test split manually and evaluate Naïve Bayes performance
import math
X = [1,2,3,4,5,6,7,8,9,10]
y = [0,0,0,0,1,1,1,1,1,1]
split = 7
X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]
class0 = [X_train[i] for i in range(len(X_train)) if y_train[i] == 0]
class1 = [X_train[i] for i in range(len(X_train)) if y_train[i] == 1]
mean0 = sum(class0) / len(class0)
mean1 = sum(class1) / len(class1)
var0 = sum((x-mean0)**2 for x in class0) / len(class0)
var1 = sum((x-mean1)**2 for x in class1) / len(class1)
prior0 = len(class0) / len(X_train)
prior1 = len(class1) / len(X_train)
def gaussian(x,m,v):
    return (1/math.sqrt(2*math.pi*v)) * math.exp(-(x-m)**2 / (2*v))
y_pred = []
for x in X_test:
    p0 = prior0 * gaussian(x, mean0, var0)
    p1 = prior1 * gaussian(x, mean1, var1)
    y_pred.append(0 if p0 > p1 else 1)
correct = 0
for i in range(len(y_test)):
    if y_test[i] == y_pred[i]:
        correct += 1
accuracy = correct / len(y_test)
print("X Train:", X_train)
print("Y Train:", y_train)
print("X Test:", X_test)
print("Y Test:", y_test)
print("Predicted:", y_pred)
print("Accuracy:", accuracy)
print("Raja Kumar Sah, 23053769")
