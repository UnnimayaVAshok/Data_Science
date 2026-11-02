"""
TRaining dataset

Student study hours,attendance,previous marks...

TRee 1          Tree 2          Tree 3

Pass            Pass            Fail

Pass - 2, Fail - 1

Majority voting

Final prediction: Pass

ML supervised algorithm to build model
It creates more than one tree(nearly 100) and combine the prediction fromm all of them
Then chooses the majority classes
It helps to reduce the overfitting in the models
Used in both classification and regression
feature scaling is usually not required
Categorical encoding should be done


Sampling
--------------
To build a single decision tree , the algorithm select random rows from our original dataset
one by one

same row can be picked more than one time

It continues until each bootstrap sample/bag reaches same size as the training data

Ths process repeated for each decison tree in the random forest

Student         Study_hours         Result
A                   1               Fail
B                   2               Fail
C                   3               Pass
D                   4               Pass
E                   5               Pass
F                   6               Fail

Tree 1
------
A       1       Fail
C       3       Pass
C       3       Pass
E       5       Pass
F       6       Fail
A       1       Fail

pass - 3,Fail - 3

Parent Gini = 1 - E p(i**2)
            = 1 - (3/6)^2 - (3/6)^2
            = 0.5

splitting
============
1,2,3,4,5,6
1.5,2.5,3.5,4.5,5.5,6.5

Identify the best split

                study_hours <= 2.5


pass - 0,fail - 2 (left node True)

Gini_left = 1 - (0/2)^2 - (2/2)^2
          = 0

pass - 3,fail -1 (right node False)

Gini_right = 1 - (3/4)^2 - (1/4)^2
           = 0.375

                number of observations in left node                     no.observations in riht node
weighted_gini = ------------------------------------ * gini_left_node + ------------------------------ * gini_right_node
                total observations in the sample                        total observations

             = (2/6)*0 + (4/6)*0.375
             = 0.25

Gini_reduction = parent_gini - weighted_gini
               = 0.5 - 0.25
               = 0.25
                ======

using gini reduction we can choose the best split(lowe gini(impurity))
using the split we need to grow the tree according to max_dept,stopping function...


TRee 2
----------
B       2       Fail
D       4       pass
F       6       Fail
B       2       Fail
E       5       Pass
C       3       Pass


from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

# n_estimators = no. of trees
# max_depth = max number of branches in each tree
# min_sample_split = min no.of samples for each split

 












"""