import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (n + 1)


def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


result = 0

for i in range(1, n + 1):
    if not visited[i]:
        if graph[i]:
            dfs(i)
            result += 1
        else:
            visited[i] = True

print(result)
