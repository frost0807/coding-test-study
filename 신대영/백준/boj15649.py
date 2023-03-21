"""
문제유형: 백트래킹
문제링크: https://www.acmicpc.net/problem/15649 
"""

# python 라이브러리로 구현 방법
from itertools import permutations

n, m = map(int, input().split())
n_list = [str(i) for i in range(1, n + 1)]

for p in list(permutations(n_list, m)):
    print(' '.join(list(p)))


# python dfs 구현
n, m = map(int, input().split())
n_list = [str(i) for i in range(1, n + 1)]
used = [False] * n  # 사용여부 체크
result = []


def dfs(k):
    if k == m:
        return print(' '.join(result))

    for i in range(n):
        if not used[i]:
            result.append(n_list[i])
            used[i] = True
            dfs(k + 1)
            used[i] = False
            result.pop()


dfs(0)
