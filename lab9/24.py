# 24. Cluster TF-IDF document vectors using K-Means and analyze cosine vs Euclidean distance effects.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
docs=["data science is fun","machine learning is powerful","football is fun","sports are exciting"]
vectorizer=TfidfVectorizer()
X=vectorizer.fit_transform(docs)
kmeans=KMeans(n_clusters=2,random_state=0)
labels=kmeans.fit_predict(X)
cos_sim=cosine_similarity(X)
print("Cluster labels:",labels)
print("Cosine similarity matrix:",cos_sim)
print("Cosine works better for text since magnitude differences matter less.")
print("Raja Kumar Sah, 23053769")