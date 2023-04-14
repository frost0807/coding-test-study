from itertools import combinations

N, M = map(int, input().split())
ALPAHBET = list(map(str, input().split()))

ALPAHBET.sort()
for a in list(combinations(ALPAHBET, N)):
    cons_count = len(set(['a', 'e', 'i', 'o', 'u']) & set(a))
    if cons_count >= 1 and N - cons_count >= 2:
        print(''.join(map(str, a)))
