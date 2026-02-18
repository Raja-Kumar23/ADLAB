# 17. Implement Naïve Bayes using log-probabilities to avoid numerical underflow

import math
X = [
    ["Sunny","Weak"],
    ["Sunny","Strong"],
    ["Overcast","Weak"],
    ["Rain","Weak"],
    ["Rain","Strong"],
    ["Overcast","Strong"]
]
y = ["No","No","Yes","Yes","No","Yes"]
classes = set(y)
priors = {}
likelihood = {}
for c in classes:
    priors[c] = math.log(y.count(c) / len(y))
for c in classes:
    likelihood[c] = {}
    for i in range(len(X[0])):
        likelihood[c][i] = {}
        values = set(x[i] for x in X)
        for v in values:
            count = 0
            for j in range(len(X)):
                if X[j][i] == v and y[j] == c:
                    count += 1
            likelihood[c][i][v] = math.log((count + 1) / (y.count(c) + len(values)))
test = ["Sunny","Weak"]
scores = {}
for c in classes:
    score = priors[c]
    for i in range(len(test)):
        score += likelihood[c][i][test[i]]
    scores[c] = score
print("Log Posterior Probabilities:", scores)
print("Predicted Class:", max(scores, key=scores.get))
print("Raja Kumar Sah, 23053769")
