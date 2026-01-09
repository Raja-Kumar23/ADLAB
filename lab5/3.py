#3. Sigmoid Function Implementation
#Write a program to:
#A. Implement the sigmoid function
#B. Plot sigmoid for values from −10 to +10
#C. Explain its role in logistic regression
import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
x = np.linspace(-10, 10, 100)
plt.plot(x, sigmoid(x))
plt.show()
print("The sigmoid function maps any real-valued number into the (0, 1) interval, making it suitable for modeling probabilities in logistic regression. It helps in transforming the linear output of the regression model into a probability score that can be used for binary classification.")
print("Raja Kumar Sah, 23053769")