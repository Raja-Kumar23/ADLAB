# 18. Write a program to visualize decision boundaries of Naïve Bayes for a 2-feature dataset
import math
import matplotlib.pyplot as plt
X = [[1,2],[2,3],[3,3],[4,5],[5,6],[6,7]]
y = [0,0,0,1,1,1]
class0 = [X[i] for i in range(len(X)) if y[i]==0]
class1 = [X[i] for i in range(len(X)) if y[i]==1]
mean0 = [sum(p[i] for p in class0)/len(class0) for i in range(2)]
mean1 = [sum(p[i] for p in class1)/len(class1) for i in range(2)]
var0 = [sum((p[i]-mean0[i])**2 for p in class0)/len(class0) for i in range(2)]
var1 = [sum((p[i]-mean1[i])**2 for p in class1)/len(class1) for i in range(2)]
prior0 = len(class0)/len(X)
prior1 = len(class1)/len(X)
def gaussian(x,m,v):
    return (1/math.sqrt(2*math.pi*v))*math.exp(-(x-m)**2/(2*v))
def predict(x1,x2):
    p0 = prior0*gaussian(x1,mean0[0],var0[0])*gaussian(x2,mean0[1],var0[1])
    p1 = prior1*gaussian(x1,mean1[0],var1[0])*gaussian(x2,mean1[1],var1[1])
    return 0 if p0>p1 else 1
xx,yy=[],[]
for i in range(0,80):
    for j in range(0,80):
        xx.append(i/10)
        yy.append(j/10)
colors=[]
for i in range(len(xx)):
    colors.append(predict(xx[i],yy[i]))
plt.scatter([p[0] for p in class0],[p[1] for p in class0])
plt.scatter([p[0] for p in class1],[p[1] for p in class1])
plt.scatter(xx,yy,c=colors,alpha=0.1)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Naïve Bayes Decision Boundary")
plt.show()
print("Raja Kumar Sah, 23053769")
