# Question 7. Manual train-test split
data = [10, 20, 30, 40, 50, 60, 70]
split_index = int(0.7 * len(data))
train = data[:split_index]
test = data[split_index:]
print("Training data:", train)
print("Testing data:", test)
print("Name: Raja Kumar")
print("Roll: 23053769")
