n_elements = int(input())
form_dict = {}

for _ in range(n_elements):
    words = input().lower().split()
    form_dict[words[0]] = []
    for i in range(1, len(words)):
        form_dict[words[0]].append(words[i])


thing = input().lower().strip()
flag = True

for key, value in form_dict.items():
    if thing in value:
        print(key)
        flag = False

if flag:
    print(f'форма "{thing}" не определена')

