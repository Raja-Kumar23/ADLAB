# 9. Write a program to compute accuracy, precision, recall, and F1-score for Naïve Bayes predictions
y_true=[1,0,1,1,0]
y_pred=[1,0,0,1,0]
tp=sum(1 for i in range(len(y_true)) if y_true[i]==y_pred[i]==1)
tn=sum(1 for i in range(len(y_true)) if y_true[i]==y_pred[i]==0)
fp=sum(1 for i in range(len(y_true)) if y_true[i]==0 and y_pred[i]==1)
fn=sum(1 for i in range(len(y_true)) if y_true[i]==1 and y_pred[i]==0)
accuracy=(tp+tn)/len(y_true)
precision=tp/(tp+fp)
recall=tp/(tp+fn)
f1=2*precision*recall/(precision+recall)
print(accuracy,precision,recall,f1)
print("Raja Kumar Sah, 23053769")
