"""
input dataset --> probabilty --> prediction

probability
===============

an event likely to be happen
0 - 1

coin >>>>> head,tail
probability(head) = 1/2 = 0.5
p(tail) = 1/2 = 0.5
p(event) = number of favourable outcomes / total number of outcomes


Types of probability
==========================

marginal probability
=====================
probability of a single event

total number of students = 10
students like python = 6
students doesnt like python = 4

p(python) = 6/10 = 0.6
p(doesnt like python) = 4/10 = 0.4

joint probability
=======================

to get the probability of two things happening together

total students = 10
who likes python = 6    A
who likes django = 4    B
students who like both python and django = 5

P(A ∩ B) = 5/10 = 0.2
probability of A and B happening together

conditional probability
===============================

measures the likelihood of an event happening given that another
related event has already occured
 
total students = 20
students know python = 10
among these 10 students who likes django = 6
p(django | python)

p(A|B) = p(A and B) / p(B)
p(A given B) = 6 / 10 = 0.6

=============================================

weather    windy     play_golf

Sunny      False     No
Sunny      True      No
Overcast   False     Yes
Rainy      False     Yes
Rainy      True      No
Overcast   True      Yes


Features --> weather = rainy,windy=False

predict --> Yes,No

                       p(Class) * p(feature_1|Class) * p(feature_2|Class)
p(Class|Features)  = -------------------------------------------------------
                                     p(Features)


                        p(Yes) * p(Rainy|Yes) * p(False|Yes)
p(Yes|Rainy,False)  = -------------------------------------------------------
                                     p(Rainy|False)


                       p(No) * p(Rainy|No) * p(False|No)
p(No|Rainy,False)  = -------------------------------------------------------
                                     p(Rainy|False)


model will predict the class which has the largest probability result
======================================================================================

                        p(Yes) * p(Rainy|Yes) * p(False|Yes)
p(Yes|Rainy,False)  = -------------------------------------------------------
                                     p(Rainy|False)

p(Yes) = 3/6 = 1/2
p(Rainy|Yes) = 1/3
p(False|Yes) = 2/3



p(Yes|Rainy,False) = 1/2 * 1/3 * 2/3 = 2/18 = 1/9 = 0.11
                                                   =======
------------------------------------------------------------------------------------


                       p(No) * p(Rainy|No) * p(False|No)
p(No|Rainy,False)  = -------------------------------------------------------
                                     p(Rainy|False)

p(No) = 3/6 = 1/2
p(Rainy|No) = 1/3
p(False|no) = 1/3



p(No|Rainy,False) = 1/2 * 1/3 * 1/3 = 1/18 = 0.05
                                             =====

here 0.11 is larger than 0.05 so our model will predict yes





















"""