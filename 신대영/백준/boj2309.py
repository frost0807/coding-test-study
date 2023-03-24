from itertools import combinations

l = [int(input()) for _ in range(9)]
l.sort()

for c in list(combinations(l, 7)):
    if sum(c) == 100:
        print('\n'.join(map(str, c)))
        break
