from itertools import permutations
n, m = map(int, input().split())

num_list = list(map(int, input().split()))

# 라이브러리 사용

temp_list = sorted(list(set(list(permutations(num_list, m)))))

for i in temp_list:
    print(' '.join(map(str, i)))

# dfs로 문제 풀이
result = []
visited = [False] * n

num_list.sort()


def dfs(depth):
    global m
    if depth == m:
        print(*result)
        return

    prev = 0
    for idx, value in enumerate(num_list):
        if not visited[idx] and prev != value:
            result.append(value)
            visited[idx] = True
            prev = value
            dfs(depth+1)
            result.pop()
            visited[idx] = False


dfs(0)
