"""
pangram is a sentence containing all letters

"""
def is_pangram(text):

    alpha = "abcdefghijklmnopqrstuvwxyz"

    for i in alpha:

        if i not in text.lower():

            print("Not pangram")
            break
    else:

        print("Pangram")

is_pangram("The quick brown fox jumps over the lazy dog")