"""
문제유형: 백트래킹
문제링크: https://www.acmicpc.net/problem/15652
"""
# python 라이브러리 구현
from itertools import combinations_with_replacement

n, m = map(int, input().split())
num_list = [str(i) for i in range(1, n + 1)]

for number in combinations_with_replacement(num_list, m):
    print(" ".join(number))

# DFS로 직접구현
n, m = map(str, input().split())
num_list = [i for i in range(1, n + 1)]
result = []


def dfs(k):
    if k == m:
        return print(' '.join(list(result)))

    for i in range(n):
        if not result or (result[k - 1] <= num_list[i]):
            result.append(num_list[i])
            dfs(k + 1)
            result.pop()


dfs(0)
