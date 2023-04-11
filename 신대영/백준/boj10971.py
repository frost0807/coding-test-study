
def dfs(start, now, dist, depth):
    global answer, n
    # 종료 조건
    if depth == n:
        if distinces[now][start]:
            dist += distinces[now][start]
            answer = min(answer, dist)
        return

    if dist > answer:
        return

    for i in range(n):
        if not visited[i] and distinces[now][i]:
            visited[i] = True
            dfs(start, i, dist + distinces[now][i], depth + 1)
            visited[i] = False


n = int(input())
distinces = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
answer = 1e9
for i in range(n):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False
print(answer)
