"""
outliers
=================
wrong values in data set or a huge deviation in values in columns


eg: height 400 ,age negative,weight negative,not possible

max value

75 percentile q3

50 percentile q2

25 percentile q1

min


working
===============

1 2 3  10 12 15 5 7 8 9 6
sort in ascending

1 2 3 5 6 7 8 9 10 12 15
median = 7 -> Q2 -> 50 percentile

take left values for Q1

1 2 3 5 6

Median = 3 -> Q1 -> 25 percentile

take right side values for Q3

8 9 10 12 15

Median = 10 -> Q3 -> 75 percentile

IQR -> Inter Quartile Range
================================
Q3 - Q1

IQR = Q3 - Q1
    = 10 -3 = 7

Top outliers = Q3 + (1.5 * IQR)
             = 10 + 10.5
             = 20.5
               
Bottom outliers = Q1 - (1.5 * IQR)
                = 3 - 10.5
                = -7.5




"""