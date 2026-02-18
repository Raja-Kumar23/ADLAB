# Question:
# Write code to compute prior, likelihood, and posterior probabilities
# for a given dataset.

X = ["Sunny", "Sunny", "Overcast", "Rain", "Rain"]
y = ["No", "No", "Yes", "Yes", "Yes"]
classes = set(y)
priors = {}
for c in classes:
    priors[c] = y.count(c) / len(y)
likelihood = {}
for c in classes:
    likelihood[c] = {}
    for val in set(X):
        count = 0
        for i in range(len(X)):
            if X[i] == val and y[i] == c:
                count += 1
        likelihood[c][val] = count / y.count(c)
test_value = "Sunny"
posterior = {}
for c in classes:
    posterior[c] = priors[c] * likelihood[c][test_value]
print("Prior Probabilities")
print(priors)
print("\nLikelihood Probabilities")
print(likelihood)
print("\nPosterior Probabilities")
print(posterior)
print("\nPredicted Class:", max(posterior, key=posterior.get))
print("Raja Kumar Sah, 23053769")
