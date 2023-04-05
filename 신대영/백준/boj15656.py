from itertools import product

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()

# 라이브러리 사용
for a in list(product(num_list, repeat=m)):
    print(' '.join(map(str, a)))

# dfs 사용
result = []


def dfs(depth):
    global m
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for num in num_list:
        result.append(num)
        dfs(depth + 1)
        result.pop()


dfs(0)
