# Snippet 1: Introduction to Machine Learning and Supervised Learning
library(caret)
lr <- train(y ~ ., data=trainData, method="lm")

# Snippet 2: Classification Algorithms
logistic <- train(y ~ ., data=trainData, method="glm")
tree <- train(y ~ ., data=trainData, method="rpart")
forest <- train(y ~ ., data=trainData, method="rf")

# Snippet 3: Unsupervised Learning
library(cluster)
kmeans <- kmeans(X, centers=3)
pca <- prcomp(X, scale. = TRUE)

# Snippet 4: Model Assessment and Evaluation Metrics
acc <- postResample(predict(logistic, testData), testData$y)
mae <- postResample(predict(lr, testData), testData$y)
