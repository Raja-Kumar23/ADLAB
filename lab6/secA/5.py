# Question:
# Given a dataset stored in a CSV file, write a program to
# A. Read data
# B. Calculate class priors
# C. Apply Naïve Bayes
# D. Predict class labels

import pandas as pd

df = pd.read_csv("data.csv")
classes = df['Play'].unique()
priors = {}
for c in classes:
    priors[c] = len(df[df['Play'] == c]) / len(df)
likelihood = {}

for col in df.columns[:-1]: 
    likelihood[col] = {}
    for val in df[col].unique():
        likelihood[col][val] = {}
        for c in classes:
            count = len(df[(df[col] == val) & (df['Play'] == c)])
            total = len(df[df['Play'] == c])
            likelihood[col][val][c] = count / total

test_data = {
    'Outlook': 'Sunny',
    'Wind': 'Weak'
}
posterior = {}
for c in classes:
    prob = priors[c]
    for col, val in test_data.items():
        prob *= likelihood[col][val][c]
    posterior[c] = prob
prediction = max(posterior, key=posterior.get)
print("Class Priors")
print(priors)
print("\nPosterior Probabilities")
print(posterior)
print("\nPredicted Class:", prediction)
print("\nRaja Kumar Sah, 23053769")
