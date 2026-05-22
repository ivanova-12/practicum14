str1 = input().lower().split()
words = {}

for word in str1:
    if word not in words:
        words[word] = 0
    words[word] += 1

sorted_words = dict(sorted(words.items(), key=lambda x: x[1], reverse=True))

for word in sorted_words:
    print(word)





