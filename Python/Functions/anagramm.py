def is_anagram(text_1,text_2):

    if len(text_1) == len(text_2):

        for i in text_1:
            if text_1.count(i) != text_2.count(i):
                print("Not anagram")
                break
        else:
                print("Anagram")
    else:
            print("Not anagram")

is_anagram("silent","listen")