from collections import deque
N, M = map(int, input().split())
graph = [list(map(str, input())) for _ in range(N)]
result = 1
answer = 1e9
distx = [0, 0, -1, 1]
disty = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            tx = x + distx[i]
            ty = y + disty[i]

            if 0 <= tx < N and 0 <= ty < M and graph[tx][ty] == '1':
                queue.append((tx, ty))
                graph[tx][ty] = str(int(graph[x][y]) + 1)

    return graph[N-1][M-1]


print(bfs(0, 0))


def dfs(x, y, depth):
    """
    dfs로 문제 풀이시 시긴초과
    """
    global result, answer, N, M

    if x == N - 1 and y == M - 1:
        answer = min(answer, result)
        return

    for i in range(4):
        tx = x + distx[i]
        ty = y + disty[i]

        if 0 <= tx < N and 0 <= ty < M and graph[tx][ty] == '1':
            result += 1
            graph[tx][ty] = '0'
            dfs(tx, ty, depth + 1)
            result -= 1
            graph[tx][ty] = '1'
