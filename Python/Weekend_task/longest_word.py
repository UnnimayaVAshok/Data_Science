# find the longest word in a sentence

sentence = input("Enter the sentence: ")

largest = 0

for i in sentence.split():

    if largest < len(i):

        largest = len(i)

        word = i

print(word)