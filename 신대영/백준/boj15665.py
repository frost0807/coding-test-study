from itertools import product
n, m = map(int, input().split())

num_list = list(map(int, input().split()))

# itertools product 라이브러리로 구현

for i in sorted(list(set(product(num_list, repeat=m)))):
    print(*i)


# dfs 알고리즘으로 구현
result_case = []
result = set()
num_list


def dfs(depth):
    global m
    if depth == m:
        t = tuple(result_case)
        if t not in result:
            result.add(t)
        return

    prev = 0
    for i, a in enumerate(num_list):
        if prev != a:
            prev = a
            result_case.append(a)
            dfs(depth + 1)
            result_case.pop()


dfs(0)
for a in sorted(list(result)):
    print(*a)
