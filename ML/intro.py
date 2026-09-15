# Machine Learning
# =====================

# machine learning >>> which enables the machine to learn the
# patterns from data and make predictions or decisions without being programmed

# Types machine learning
# ===========================

# supervised learning
# ====================

# Type of machine learning in which a model learns from labeled data
# where the input and expected output are provide during training

# Classification
# ==========================
# classification is a type of supervised learning used to predict a category
# eg: Iris,disease classification

# Regression
# =====================
# regression is a type of supervised learning used to predict the 
# continuous numerical value
# eg: houseprice,tempearture,sale prediction

# Algorithms
# ===================

# KNN - K nearest neighbour >>> classification,regression
# ==========================================================

# a supervised learning algorithm that predict the output of a new point
# looking at its nearest data points in the training dataset

# | Student | Hours studied | Attendence | Result  |
# | ------- | ------------- | ---------- | ------  |
# |   A     |        1      |     50     |  Fail   |
# |   B     |        2      |     55     |  Fail   |
# |   C     |        3      |     60     |  Fail   |
# |   D     |        5      |     75     |  Pass   |
# |   E     |        6      |     80     |  Pass   |
# |   F     |        7      |     90     |  Pass   |


# new point g (5,78) (x1,y1)
# first point A (1,50) (x2,y2)

# Euclidean distance formula
# =================================

# d = sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
# 
# sqrt{(1 - 5)^2 + (50 -70)^2} = sqrt(3.78)

# 3.1,2.9,2.4,0.5,1.3,2.5
# 0.5,1.3,2.4,2.5,2.9,3.1

# k = 5
# 0.5,1.3,2.4,2.5,2.9
# pass,pass,pass,fail,fail
# it chooses pass at the majority is pass
# pass count = 3
# fail count = 2

# k = 3
# it chooses 3 of them and choose the
# majority

# unsupervised
# ===================

# Type of learning where the machine learns the patterns from the data without the
# expected output
# customer segmentation
# accuracy score


# unsupervised algorithms
# =======================

# Kmeans clustering

# Classification algorithms
# ==========================
# KNN               >>> Distance formula | 
# Naive bayes       >>> probability
# decision tree     >>> 
# Random forest     >>>
# Xg boosting       >>> 

# Regression algorithms
# ===========================
# Linear regression
# Polynomial

# reinforcement
# ===============
# 