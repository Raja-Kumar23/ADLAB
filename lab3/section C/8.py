# Question 8. Pie chart
import matplotlib.pyplot as plt
categories = ["Food", "Rent", "Transport", "Others"]
values = [40, 30, 20, 10]
plt.pie(values, labels=categories, autopct="%1.1f%%")
plt.title("Expense Distribution")
plt.show()
print("Name: Raja Kumar")
print("Roll: 23053769")
