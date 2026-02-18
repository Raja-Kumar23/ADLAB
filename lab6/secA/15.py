# 15. Implement Bernoulli Naïve Bayes and compare it with Multinomial NB

docs = [
    "good movie",
    "good acting",
    "bad movie",
    "bad acting"
]
labels = ["pos","pos","neg","neg"]
vocab = set()
for d in docs:
    vocab.update(d.split())
bern_count = {}
class_count = {}
for i in range(len(docs)):
    c = labels[i]
    class_count[c] = class_count.get(c,0) + 1
    bern_count.setdefault(c,{})
    words = set(docs[i].split())
    for w in vocab:
        bern_count[c][w] = bern_count[c].get(w,0) + (1 if w in words else 0)
test = "good movie".split()
bern_score = {}
for c in class_count:
    p = class_count[c] / len(docs)
    for w in vocab:
        if w in test:
            p *= (bern_count[c][w] + 1) / (class_count[c] + 2)
        else:
            p *= (class_count[c] - bern_count[c][w] + 1) / (class_count[c] + 2)
    bern_score[c] = p
multi_count = {}
for i in range(len(docs)):
    c = labels[i]
    multi_count.setdefault(c,{})
    for w in docs[i].split():
        multi_count[c][w] = multi_count[c].get(w,0) + 1
multi_score = {}
for c in class_count:
    p = class_count[c] / len(docs)
    total_words = sum(multi_count[c].values())
    for w in test:
        p *= (multi_count[c].get(w,0) + 1) / (total_words + len(vocab))
    multi_score[c] = p
print("Bernoulli NB Prediction:", max(bern_score, key=bern_score.get))
print("Multinomial NB Prediction:", max(multi_score, key=multi_score.get))
print("Raja Kumar Sah, 23053769")
