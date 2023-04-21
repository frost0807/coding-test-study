from collections import deque
C = int(input())

# 나이트가 움직일 수 있는 범위
dist = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


def bfs(x, y):
    global t_x, t_y, N

    queue = deque()
    queue.append((x, y, 0))

    while queue:
        x, y, depth = queue.popleft()

        if x == t_x and y == t_y:
            print(depth)
            break

        for dx, dy in dist:
            mx = x + dx
            my = y + dy

            if 0 <= mx < N and 0 <= my < N and graph[mx][my] != 1:
                graph[mx][my] = 1
                queue.append((mx, my, depth + 1))


for _ in range(C):
    N = int(input())
    graph = [[0] * N for _ in range(N)]
    s_x, s_y = map(int, input().split())
    t_x, t_y = map(int, input().split())

    graph[s_x][s_y] = 1
    bfs(s_x, s_y)
