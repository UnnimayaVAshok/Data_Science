def count_words(text):
    count = 1
    for i in text:
        if i == " ":
            count += 1
    return count
print(count_words("Python Full Stack Development"))