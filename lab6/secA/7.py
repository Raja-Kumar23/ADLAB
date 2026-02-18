# 7. Implement Laplace smoothing in Naïve Bayes and show its effect on zero probabilities
docs = ["good movie", "good acting"]
labels = ["pos", "pos"]
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
test_word = "bad"
prob_without = word_count["pos"].get(test_word, 0) / sum(word_count["pos"].values())
prob_with = (word_count["pos"].get(test_word, 0) + 1) / (sum(word_count["pos"].values()) + len(vocab))
print("Probability without Laplace:", prob_without)
print("Probability with Laplace:", prob_with)
print("Raja Kumar Sah, 23053769")
