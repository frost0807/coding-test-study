"""
문제유형: 백트래킹
문제링크: https://www.acmicpc.net/problem/15654
"""
# 라이브러리 버전
from itertools import permutations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

for p in list(permutations(num_list, m)):
    print(' '.join(map(str, list(p))))


# 직접구현
input = sys.stdin.readline
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
used = [False] * n
result = []


def dfs(k):
    if k == m:
        return print(' '.join(map(str, result)))

    for i in range(n):
        if not used[i]:
            result.append(num_list[i])
            used[i] = True
            dfs(k + 1)
            used[i] = False
            result.pop()


# 먼저 정렬하고 DFS 호출
num_list.sort()
dfs(0)
