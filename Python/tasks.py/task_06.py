# 5)Given a pattern**

#  Text=”ABABC”**

#  Write a program to print first non-recursive character output=c without using nested loop**

text = "ABABC"

print([i for i in text if text.count(i) == 1])