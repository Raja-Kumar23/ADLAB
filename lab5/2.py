#2. Logistic Regression Using scikit-learn
#Load a binary classification dataset and:
#A. Train a Logistic Regression model
#B. Print coefficients and intercept
#C. Predict probabilities and class labels
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
X, y = make_classification(
    n_samples=5,
    n_features=1,
    n_informative=1,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=1
)
model = LogisticRegression()  #create logistic regression model
model.fit(X, y)
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
print("Probabilities:", model.predict_proba(X))
print("Class labels:", model.predict(X))
print("Raja Kumar Sah, 23053769")