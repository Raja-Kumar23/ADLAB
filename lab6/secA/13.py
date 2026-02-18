# 13. Implement Multinomial Naïve Bayes for document classification
docs = [
    "good movie good acting",
    "good direction movie",
    "bad movie boring",
    "bad acting boring"
]
labels = ["pos","pos","neg","neg"]
class_count = {}
word_count = {}
vocab = set()
for i in range(len(docs)):
    c = labels[i]
    class_count[c] = class_count.get(c,0) + 1
    word_count.setdefault(c,{})
    for w in docs[i].split():
        vocab.add(w)
        word_count[c][w] = word_count[c].get(w,0) + 1
test = "good movie".split()
scores = {}
for c in class_count:
    p = class_count[c] / len(docs)
    total_words = sum(word_count[c].values())
    for w in test:
        p *= (word_count[c].get(w,0) + 1) / (total_words + len(vocab))
    scores[c] = p
print("Predicted Class:", max(scores, key=scores.get))
print("Raja Kumar Sah, 23053769")
