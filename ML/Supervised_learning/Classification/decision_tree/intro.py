"""
Decision tree
======================
Supervised ml algorithm used for classification and regression.
It make the prediction by series of decision rules in tree like structure.

dataset >> input,output

using this dataset (features and target) we build a tree like structure
using this data structure we make the predictions.

impurity
===============
Mesures how mixed or uncertain the classes in a target column (node)

Entropy
===================
Measure of impurity in a dataset

Entropy = -E plog(p)               p >>> probabilty of class in target

for binary class
=========================

Entropy = -(p(pass) * log_2(p(pass)) + (p(fail) * log_2(p(fail)) )


Age        Ex        Pizza         fit/unfit
30         no         yes            unfit
40         yes        yes            fit
35         no         no             fit
32         yes        no             fit


node >>> root node,intermediate node

node >>> features
leafs >>> target classes

age 36 no yes
age 45 yes yes

                          age > 40
                         ----------------
                        |              |       
                    yes |              |no                                                        
                        |              |
                    -----------      ---------                                                                                                                    
                       ex              pizza   
                    ----------       ----------                                                                                                     
                   |        |         |       |                                                                                                  
                yes|        |no    yes|       |no                                                                                                 
                   |        |         |       | 
                 ------   -------  ------     ---------                                                                                                
                  fit      unfit   unfit       fit                                                                                                                        
                                                                                                                                             
                                                                                                                                             
                                                                                                                                             
Height           weight           label
170                75              female                                                                                                             
170                90               male                                                                                                    
185                85               male                                                                                                       
155                50              female                                                                                                        
175                70              female    

185 90
Divide and Conquer
==========================

top down strategy used to build a tree by splitting the dataset into smaller,based on features

Entropy(S) = - p(0)log2p(0) - p(1)log2(p1)

                                          height > 180                                                                                                      |
                                -------------------------------------
                        true    |                                   |   false
                                |                                   |
                        185 85 male                         170 75 female
                                                            170 90 male
                                                            155 50 female
                                                            175 70 female
                                                                  |
                                                                  |
                                                            weight > 80
                                                        -------------------
                                                   true |                  |  false
                                                        |                  |
                                                    170 90 male        170 75 female
                                                                       155 50 female
                                                                       175 70 female
                                          
                                          
                                         height > 180                                                                                                      |
                                -------------------------------------
                        true    |                                   |   false
                                |                                   |
                               male                           weight > 80
                                                        -------------------
                                                   true |                  |  false
                                                        |                  |
                                                       male              female
                                                                       
                                          
                                          
output  >> target
0 - 14
1 - 9

impurity always between 0 and 1
1 >> target in mixed classes
0 >> target remain in single class

parent entropy
==================
p(0) = 14/23 = 0.60

p(1) = 9 /23 = 0.39
                                          
Entropy(S) = - p(0)log2p(0) - p(1)log2(p1)
           = -0.08                                        

======================================================

outlook     windy       play
Sunny       False       No
Sunny       True        No
Overcast    False       Yes
Rain        False       Yes
Rain        True        No
Overcast    True        Yes

Gini,Entropy

p(yes) = 1/2
p(no) = 1/2
parent entropy = -p(yes)log2p(yes) - p(no)log2p(no)
               =  1

feature column
==================
outlook >>> split >>> sunny,overcast,rain
---------------------------------------------

sunny >>> no - 2 , yes - 0

p(no) = 2/2

entropy = -p(no)log2p(no) - p(yes)log2p(yes)
        = 0

overcast >>> no - 0 , yes - 2

entropy = -p(no)log2p(no) - p(yes)log2p(yes)
        = 0

rain >>> no - 1 , yes - 1

entropy = -p(no)log2p(no) - p(yes)log2p(yes)
        = - 1/2 log2(1/2) - 1/2 log2(1/2)
        = 1
 
weighted_entropy_outlook = 2/6 * 0 + 2/6 * 0 + 2/6 * 1
                         = 1/3 = 0.33

information_gain_outlook = parent_entropy - weighted_entropy_outlook
                         = 1 - 0.33
                         = 0.67  

windy >>> split >>> True , False

True >> no -2, yes - 1

entropy = -p(no)log2(p(no)) - p(yes)log2(p(yes))
        = -2/3 log2(2/3) - 1/3 log2(1/3)
        = 0.91

False >>> no - 1 , yes - 2

entropy = -p(no)log2(p(no)) - p(yes)log2(p(yes))
        = -(1/3)log2(1/3) - 2/3log2(2/3)
        = 0.91

weighted_entropy_windy = 3/6 * 0.91 + 3/6 * 0.91
                       = 0.91

information_gain_windy =  parent_entropy - weighted_entropy_outlook
                       = 1 - 0.91
                       = 0.09

root node = feature with highest information gain

root node = outlook

                                        outlook
                                      -----------
                                      |    |     |
                                      s    o     r

outlook     windy       play
________________________________
sunny       True        No
sunny       False       No              yes - 0 , No - 2
overcast    True        Yes
overcast    False       yes             yes - 2 , No - 0
rainy       True        No
rainy       False       Yes             yes - 1 , No - 1 


entropy(rainy) = -.5log2(.5) - .5log2(.5)
               = 1

rainy,windy = false >>> yes - 1 , no - 0
entropy = 0

rainy,windy = true >>> yes - 0 , no - 1
entropy = 0


                                        outlook
                                      -----------
                                      |    |     |
                                      s    o     r
                                      |    |     |
                                      No  Yes    |
                                               windy
                                              |     |
                                              |     |
                                             True  False
                                              |      |
                                              No    Yes


                                              
selecting root node
========================
considering the categories from root node
sunny >> entropy >> 0
overcast >> entropy >> 0
rain >> entropy >> 1 - need a split

rain use windy
windy >> false >> yes
windy >> true >> no




"""

