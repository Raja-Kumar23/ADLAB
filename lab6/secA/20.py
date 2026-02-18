# 20. Write a program to implement Naïve Bayes using k-fold cross-validation

X = [12,15,18,20,22,25,28,30,32,35,38,40,42,45,48,50,52,55,58,60]
y = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
k = 5
size = len(X) // k
for i in range(k):
    test_X = X[i*size:(i+1)*size]
    train_X = X[:i*size] + X[(i+1)*size:]
    test_y = y[i*size:(i+1)*size]
    train_y = y[:i*size] + y[(i+1)*size:]
    print("Fold", i+1)
    print("Train X:", train_X)
    print("Test X:", test_X)
    print("Train y:", train_y)
    print("Test y:", test_y)
    print()
print("Raja Kumar Sah, 23053769")
