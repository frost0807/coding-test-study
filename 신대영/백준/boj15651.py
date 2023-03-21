"""
문제유형: 백트래킹
문제링크: https://www.acmicpc.net/problem/15651
"""
# python 라이브리러 사용
from itertools import product

n, m = map(int, input().split())
num_list = [str(i) for i in range(1, n + 1)]

for p in list(product(num_list, repeat=m)):
    print(' '.join(list(p)))


# 직접구현 DFS로 구현
n, m = map(int, input().split())
num_list = [str(i) for i in range(1, n + 1)]
result = []


def dfs(k):
    if k == m:
        return print(' '.join(list(result)))

    for i in range(n):
        result.append(num_list[i])
        dfs(k + 1)
        result.pop()


dfs(0)
