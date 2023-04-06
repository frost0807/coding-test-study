from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = sorted(list(map(int, input().split())))

# 라이브러리 사용
for a in sorted(list(set(combinations(num_list, m)))):
    print(*a)


# dfs 알고리즘 사용해서 처리
result = []
visited = [False] * n


def dfs(depth, n_list):
    if depth == m:
        print(*result)
        return

    prev = 0
    for i, v in enumerate(n_list):
        if prev != v:
            result.append(v)
            prev = v
            dfs(depth + 1, n_list[i+1:])
            result.pop()


dfs(0, num_list)
