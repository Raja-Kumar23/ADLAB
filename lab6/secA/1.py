import pandas as pd
data = {
    'Outlook': [
        'Sunny','Sunny','Overcast','Rain','Rain','Rain','Sunny','Overcast',
        'Overcast','Rain','Sunny','Rain','Overcast','Sunny','Rain'
    ],
    'Wind': [
        'Weak','Strong','Weak','Weak','Weak','Strong','Weak','Strong',
        'Weak','Strong','Strong','Weak','Strong','Weak','Strong'
    ],
    'Play': [
        'No','No','Yes','Yes','Yes','No','No','Yes',
        'Yes','No','No','Yes','Yes','No','No'
    ]
}
df = pd.DataFrame(data)
def train_nb(df):
    classes = df['Play'].unique()
    priors = {}
    likelihood = {}
    for c in classes:
        priors[c] = len(df[df['Play'] == c]) / len(df)
    for col in df.columns[:-1]:
        likelihood[col] = {}
        for val in df[col].unique():
            likelihood[col][val] = {}
            for c in classes:
                count = len(df[(df[col] == val) & (df['Play'] == c)])
                total = len(df[df['Play'] == c])
                likelihood[col][val][c] = count / total
    return priors, likelihood, classes
priors, likelihood, classes = train_nb(df)
test_data = {'Outlook': 'Sunny', 'Wind': 'Weak'}
posterior = {}
for c in classes:
    prob = priors[c]
    for col, val in test_data.items():
        prob *= likelihood[col][val][c]
    posterior[c] = prob
prediction = max(posterior, key=posterior.get)
print("Prior Probabilities")
print(priors)
print("\nPosterior Probabilities")
print(posterior)
print("\nPredicted Class:", prediction)
print("\nRaja Kumar Sah, 23053769")
