words = ["Python", "java", "PYTHON", "Java", "C", "c"]

for i in range(0,len(words)):

    words[i] = words[i].lower()

for i in words:
    
    if words.count(i) > 1:
        for j in range(words.count(i) - 1):
            words.remove(i)
    if i not in words:
        words.append(i)

print(words)