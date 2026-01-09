# Question 7. Multiple line plot
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5]
sales_2023 = [10, 20, 30, 40, 50]
sales_2024 = [15, 25, 35, 45, 55]
sales_2025 = [20, 30, 40, 50, 60]
plt.plot(months, sales_2023, label="2023")
plt.plot(months, sales_2024, label="2024")
plt.plot(months, sales_2025, label="2025")
plt.legend()
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Comparison")
plt.show()
print("Name: Raja Kumar")
print("Roll: 23053769")
