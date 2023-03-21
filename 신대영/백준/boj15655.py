"""
문제유형: 백트래킹
문제링크: https://www.acmicpc.net/problem/15655
"""
# 라이브러리 구현
import sys
from itertools import combinations
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

for c in list(combinations(num_list, m)):
    print(' '.join(map(str, c)))

# 직접구현
input = sys.stdin.readline
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
result = []


def dfs(k, start):
    if k == m:
        return print(' '.join(map(str, result)))

    for i in range(start, n):
        if i == 0 or num_list[i - 1] != num_list[i]:
            result.append(num_list[i])
            dfs(k + 1, i + 1)
            result.pop()


# 먼저 정렬하고 DFS 호출
num_list.sort()
dfs(0, 0)
