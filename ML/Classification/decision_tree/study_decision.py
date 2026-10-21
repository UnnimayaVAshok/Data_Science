"""
study       internet        pass
-------------------------------------
High        Good            yes
High        Poor            yes
High        Good            yes
High        Poor            no
Low         Good            no
Low         Poor            no
Low         Good            no
Low         Poor            no

p(yes) = 3/8
p(no) = 5/8
parent entropy = -p(yes)log2(p(yes)) - p(no)log2(p(no))
               = -(3/8)log2(3/8) - (5/8)log2(5/8)
               = 0.95

study split
============
high = 4  yes = 3 , no = 1 
low = 4   yes = 0 , no = 4

entropy(high) = -(3/4)log2(3/4) - (1/4)log2(1/4)
              = 0.811
entropy(low) = -(4/4)log2(4/4) - 0
             = 0 

weighted_entropy = 4/8 * 0.811 + 4/8 * 0
                 = 0.405

information_gain = 0.95 - 0.405
                 = 0.544

internet split
================
good = 4 , yes = 2 , no = 2
poor = 4 , yes = 1 , no = 3

entropy(good) = -(2/4)log2(2/4) - (2/4)log2(2/4)
              = 1
entropy(poor) = -(1/4)log2(1/4) - (3/4)log2(3/4)
              = 0.811

weighted_entropy = 4/8 * 1 + 4/8 * 0.811
                 = 0.905

information_gain = 0.95 - 0.905
                 = 0.044

root node is study
==========================

high = 4  yes = 3 , no = 1 
low = 4   yes = 0 , no = 4

entropy(high) = -(3/4)log2(3/4) - (1/4)log2(1/4)
              = 0.811
entropy(low) = -(4/4)log2(4/4) - 0
             = 0 

                                       study
                                ---------------------
                                |                   |
                                high               low
                                 |                  |
 selecting next feature       internet             No
    internet                -------------
                            |           |
                          Good         Poor
                            |           |
                           Yes
high , internet = good

yes - 3, no 0
entropy = 0

high , internet = poor

yes = 1,no = 1
entropy = 1

selecting next feature







"""