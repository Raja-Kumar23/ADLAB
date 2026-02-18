# 16. Write a program to classify emails as spam or ham using Naïve Bayes
emails = [
    "win prize now",
    "limited offer win",
    "hello friend how are you",
    "let us meet tomorrow",
    "win money prize",
    "are you coming today"
]
labels = ["spam","spam","ham","ham","spam","ham"]
class_count = {}
word_count = {}
vocab = set()
for i in range(len(emails)):
    c = labels[i]
    class_count[c] = class_count.get(c,0) + 1
    word_count.setdefault(c,{})
    words = emails[i].split()
    for w in words:
        vocab.add(w)
        word_count[c][w] = word_count[c].get(w,0) + 1
test = "win money now".split()
scores = {}
for c in class_count:
    p = class_count[c] / len(emails)
    for w in test:
        p *= (word_count[c].get(w,0) + 1) / (sum(word_count[c].values()) + len(vocab))
    scores[c] = p
print("Predicted Class:", max(scores, key=scores.get))
print("Raja Kumar Sah, 23053769")
