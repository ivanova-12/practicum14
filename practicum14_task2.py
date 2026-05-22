n_pairs = int(input())
english_dict = {}

for _ in range(n_pairs):
    pair = input().lower().split()
    english_dict[pair[0]] = pair[1]

phrase = input().strip().lower().split()
translated_phrase = ''

for word in phrase:
    if word in english_dict:
        translated_phrase += ' ' + english_dict[word]
    else:
        translated_phrase += ' ' + word

print(translated_phrase.strip())

