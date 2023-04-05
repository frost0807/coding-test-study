from itertools import combinations_with_replacement

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()

# 라이브러리로 문제 풀이
for a in list(combinations_with_replacement(num_list, m)):
    print(' '.join(map(str, a)))

# dfs로 문제 풀이
result = []


def dfs(depth, n_list):
    global m
    if depth == m:
        print(" ".join(map(str, result)))
        return

    for idx, num in enumerate(n_list):
        result.append(num)
        dfs(depth + 1, n_list[idx:])
        result.pop()


dfs(0, num_list)
