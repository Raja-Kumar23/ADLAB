# Question:
# Write a program to classify a new data point using Naïve Bayes given
# A. Prior probabilities
# B. Conditional probabilities
priors = {
    "Yes": 0.6,
    "No": 0.4
}
conditional = {
    "Yes": {
        "Sunny": 0.2,
        "Weak": 0.7
    },
    "No": {
        "Sunny": 0.6,
        "Weak": 0.4
    }
}
test_data = ["Sunny", "Weak"]
posterior = {}
for c in priors:
    prob = priors[c]                
    prob *= conditional[c]["Sunny"] 
    prob *= conditional[c]["Weak"]
    posterior[c] = prob

predicted_class = max(posterior, key=posterior.get)
print("Posterior Probabilities:", posterior)
print("Predicted Class:", predicted_class)
print("Raja Kumar Sah, 23053769")
