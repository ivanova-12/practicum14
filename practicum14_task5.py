n_parent_relations = int(input())
relations_dict = {}

for _ in range(n_parent_relations):
    pair = input().lower().split()

    if pair[0] not in relations_dict:
        relations_dict[pair[0]] = [pair[1]]
    else:
        relations_dict[pair[0]].append(pair[1])

name = input().lower().strip()


def count_descendants(ancestor: str) -> int:
    if ancestor not in relations_dict:
        return 0
    result = 0
    for descendant in relations_dict[ancestor]:
        result += 1 + count_descendants(descendant)
    return result

if __name__ == '__main__':
    print(count_descendants(name))

