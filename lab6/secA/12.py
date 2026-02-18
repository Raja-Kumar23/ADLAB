# 12. Write code to demonstrate how Naïve Bayes behaves when features are strongly correlated
import math
X = [
    [1,1],
    [2,2],
    [3,3],
    [4,4]
]
y = [0,0,1,1]
class0 = [X[i] for i in range(len(X)) if y[i] == 0]
class1 = [X[i] for i in range(len(X)) if y[i] == 1]
mean0 = [sum(p[i] for p in class0)/len(class0) for i in range(2)]
mean1 = [sum(p[i] for p in class1)/len(class1) for i in range(2)]
var0 = [sum((p[i]-mean0[i])**2 for p in class0)/len(class0) for i in range(2)]
var1 = [sum((p[i]-mean1[i])**2 for p in class1)/len(class1) for i in range(2)]
prior0 = len(class0)/len(X)
prior1 = len(class1)/len(X)
def gaussian(x,m,v):
    return (1/math.sqrt(2*math.pi*v))*math.exp(-(x-m)**2/(2*v))
test = [2.5,2.5]
p0 = prior0
p1 = prior1
for i in range(2):
    p0 *= gaussian(test[i], mean0[i], var0[i])
    p1 *= gaussian(test[i], mean1[i], var1[i])
prediction = 0 if p0 > p1 else 1
print("Predicted Class:", prediction)
print("Raja Kumar Sah, 23053769")
