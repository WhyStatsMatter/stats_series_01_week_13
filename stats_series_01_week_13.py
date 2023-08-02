# Snippet 1: Introduction to Machine Learning and Supervised Learning
from sklearn.linear_model import LinearRegression
lr = LinearRegression().fit(X_train, y_train)

# Snippet 2: Classification Algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

logistic = LogisticRegression().fit(X_train, y_train)
tree = DecisionTreeClassifier().fit(X_train, y_train)
forest = RandomForestClassifier().fit(X_train, y_train)

# Snippet 3: Unsupervised Learning
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

kmeans = KMeans(n_clusters=3).fit(X)
pca = PCA(n_components=2).fit_transform(X)

# Snippet 4: Model Assessment and Evaluation Metrics
from sklearn.metrics import accuracy_score, mean_absolute_error

acc = accuracy_score(y_test, logistic.predict(X_test))
mae = mean_absolute_error(y_test, lr.predict(X_test))
