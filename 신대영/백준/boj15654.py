"""
문제유형: 백트래킹
문제링크: https://www.acmicpc.net/problem/15654
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
used = [False] * n
result = []


def dfs(k):
    if k == m:
        return print(' '.join(result))

    for i in range(n):
        if not used[i]:
            result.append(str(num_list[i]))
            used[i] = True
            dfs(k + 1)
            used[i] = False
            result.pop()


# 먼저 정렬하고 DFS 호출
num_list.sort()
dfs(0)
