"""
def recursive(text):

    for i in text:

        if text.count(i) > 1:

            print(i)
            break

def recursive(text):

    new = ""

    for i in text:

        if i not in new:

            if text.count(i) > 1:

                new += i

        print(i,text.count(i))
"""
def recursive(text):

    for i in text:

        if text.count(i) == 1:

            print(i)
            break

recursive("AABBCDAB")
