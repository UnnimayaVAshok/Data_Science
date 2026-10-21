"""
accuract_score
==================
tp + tN/tp+tn+fp+fn
Recall
================
out of all actual positive cases how many did the model predited correctly(TP)

recall = TP / TP + FN
recall = TN /TN + FP
Precision
=================
out of all cases the model predicted as positive how many of them are actually positive

precision = TP / TP + FP
precision = TN / TN + FN

F1-Score
==================

              2 * (recall 1 * precision 1)
f1-score 1 =      ------------------------
                  (recall 1 + precision 1)


              2 * (recall 0 * precision 0)
f1-score 0 =      ------------------------
                  (recall 0 + precision 0)

                        recall(1) + racall(0)
macro_avg recall = ---------------------------
                                  2


                        precision(1) + precision(0)
macro_avg precision = ---------------------------
                                  2

                   ( recall(1) * support(1) ) + ( recall(0) * support(0) )     
weighted_avg recall = ----------------------------------------------------------
                                  total number of support



                   ( precision(1) * support(1) ) + ( precision(0) * support(0) )     
weighted_avg precision = ----------------------------------------------------------
                                  total number of support


macro - average
============================

Get a single f1 by considering equal weight to both class

           f1(0) + f1(1)
macrof1 = -------------------
                 2

                 ( f1_0 * support_0 ) + ( f1_1 * support_1 )
weighted_avg = ----------------------------------------------------
                      support_0 + support_1







"""