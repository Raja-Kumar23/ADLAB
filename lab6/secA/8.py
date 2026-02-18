# 8. Write a program to compare classification results with and without Laplace smoothing
docs = ["good movie", "bad movie", "good acting", "bad acting"]
labels = ["pos", "neg", "pos", "neg"]
class_count = {}
word_count = {}
vocab = set()
for i in range(len(docs)):
    c = labels[i]
    class_count[c] = class_count.get(c, 0) + 1
    word_count.setdefault(c, {})
    for w in docs[i].split():
        vocab.add(w)
        word_count[c][w] = word_count[c].get(w, 0) + 1
test = "good movie".split()
scores_without = {}
for c in class_count:
    p = class_count[c] / len(docs)
    for w in test:
        if w in word_count[c]:
            p *= word_count[c][w] / sum(word_count[c].values())
        else:
            p = 0
    scores_without[c] = p
scores_with = {}
for c in class_count:
    p = class_count[c] / len(docs)
    total_words = sum(word_count[c].values())
    for w in test:
        p *= (word_count[c].get(w, 0) + 1) / (total_words + len(vocab))
    scores_with[c] = p
print("Prediction without Laplace:", max(scores_without, key=scores_without.get))
print("Prediction with Laplace:", max(scores_with, key=scores_with.get))
print("Raja Kumar Sah, 23053769")
