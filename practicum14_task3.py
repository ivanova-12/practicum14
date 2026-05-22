n_elements = int(input())
antonyms_dict = {}

for _ in range(n_elements):
    pair = input().lower().split()
    antonyms_dict[pair[0]] = pair[1]
    antonyms_dict[pair[1]] = pair[0]

word = input().lower().strip()

if word in antonyms_dict:
    print(antonyms_dict[word])
else:
    print(word)

