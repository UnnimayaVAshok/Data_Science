def is_anagram(text_1,text_2):
    if len(text_1) != len(text_2):
        return "Not anagram"
    for i in text_2:
        if i in text_1:
            anagram = True
        else:
            anagram = False
            break
    if anagram == True:
        return "Anagram"
    else:
        return "Not Anagram"
print(is_anagram("listen","silent"))