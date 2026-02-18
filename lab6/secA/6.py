# 6. Write a Python program to implement Naïve Bayes for text classification using word frequencies (no library)
docs=["good movie","bad movie","good acting","bad acting"]
labels=["pos","neg","pos","neg"]
class_count={}
word_count={}
for i in range(len(docs)):
    c=labels[i]
    class_count[c]=class_count.get(c,0)+1
    word_count.setdefault(c,{})
    for w in docs[i].split():
        word_count[c][w]=word_count[c].get(w,0)+1
test="good movie".split()
score={}
for c in class_count:
    p=class_count[c]/len(docs)
    for w in test:
        p*=word_count[c].get(w,1)
    score[c]=p
print(max(score,key=score.get))
print("Raja Kumar Sah, 23053769")
