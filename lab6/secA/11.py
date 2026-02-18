# 11. Write a program to display the confusion matrix for Naïve Bayes classifier
y_true = [1, 0, 1, 1, 0, 0, 1]
y_pred = [1, 0, 0, 1, 0, 1, 1]
tp = 0
fp = 0
fn = 0
tn = 0
for i in range(len(y_true)):
    if y_true[i] == 1 and y_pred[i] == 1:
        tp += 1
    elif y_true[i] == 0 and y_pred[i] == 1:
        fp += 1
    elif y_true[i] == 1 and y_pred[i] == 0:
        fn += 1
    else:
        tn += 1
confusion_matrix = [
    [tp, fp],
    [fn, tn]
]
print("Confusion Matrix:")
print(confusion_matrix)
print("Raja Kumar Sah, 23053769")
