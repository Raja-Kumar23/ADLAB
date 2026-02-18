# 14. Write a program to demonstrate why Naïve Bayes works well even when independence assumption is violated
X=[[1,1],[2,2],[3,3],[4,4]]
y=[0,0,1,1]
import math
def g(x,m,v): return (1/math.sqrt(2*math.pi*v))*math.exp(-(x-m)**2/(2*v))
c0=[X[i] for i in range(len(X)) if y[i]==0]
c1=[X[i] for i in range(len(X)) if y[i]==1]
m0=[sum(f[i] for f in c0)/len(c0) for i in range(2)]
m1=[sum(f[i] for f in c1)/len(c1) for i in range(2)]
v0=[sum((f[i]-m0[i])**2 for f in c0)/len(c0) for i in range(2)]
v1=[sum((f[i]-m1[i])**2 for f in c1)/len(c1) for i in range(2)]
test=[2.5,2.5]
p0=len(c0)/len(X)
p1=len(c1)/len(X)
for i in range(2):
    p0*=g(test[i],m0[i],v0[i])
    p1*=g(test[i],m1[i],v1[i])
print(0 if p0>p1 else 1)
print("Raja Kumar Sah, 23053769")
