"""
one hot encoding only after x,y separation

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder

col_data = make_column_transformer((OneHotEncoder(handle_unknown="ignore),["State"]),remainder="passthrough")
# handle unknown is used to ignore data which is not trained or not present in State column
# remainder is used to remain the other column itself

drwback - more number of columns forms hence overfit

to overcome use get dummies


get dummies and label encoding done before x,y separation

like one hot but 1st column is droped

friuts      apple       grape       mango       orange

apple          1            0       0              0

orange          0           0       0               1

mango           0           0       1               0

grape           0           1       0               0

drop apple column...........






label-drwback-form a heirarchy


"""