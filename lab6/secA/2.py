# Question:
# Implement Gaussian Naïve Bayes without using any ML library.
# Compute mean, variance, and posterior probability manually.

import math
X = [1, 2, 3, 6, 7, 8]
y = [0, 0, 0, 1, 1, 1]
class0 = []
class1 = []
for i in range(len(X)):
    if y[i] == 0:
        class0.append(X[i])
    else:
        class1.append(X[i])
mean0 = sum(class0) / len(class0)
mean1 = sum(class1) / len(class1)
var0 = sum((x - mean0) ** 2 for x in class0) / len(class0)
var1 = sum((x - mean1) ** 2 for x in class1) / len(class1)
prior0 = len(class0) / len(X)
prior1 = len(class1) / len(X)
def gaussian(x, mean, var):
    return (1 / math.sqrt(2 * math.pi * var)) * math.exp(-(x - mean) ** 2 / (2 * var))
test_value = 4
posterior0 = prior0 * gaussian(test_value, mean0, var0)
posterior1 = prior1 * gaussian(test_value, mean1, var1)
if posterior0 > posterior1:
    print("Predicted Class: 0")
else:
    print("Predicted Class: 1")
print("Raja Kumar Sah, 23053769")
