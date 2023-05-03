from collections import deque
import sys
input = sys.stdin.readline


def get_start_point():
    global tomato_count
    start_point = []
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                start_point.append((i, j, 0))
            elif graph[i][j] == 0:
                tomato_count += 1

    return start_point


def bfs():
    global result, tomato_count
    queue = deque(get_start_point())

    while queue:
        x, y, day = queue.popleft()

        for dx, dy in dist:
            tx = x + dx
            ty = y + dy

            if 0 <= tx < M and 0 <= ty < N and not graph[tx][ty]:
                graph[tx][ty] = 1
                tomato_count -= 1
                result = max(result, day + 1)
                queue.append((tx, ty, day + 1))


N, M = map(int, input().split())  # NxM 그래프
graph = [list(map(int, input().split())) for _ in range(M)]
dist = [(0, -1), (0, 1), (1, 0), (-1, 0)]
result = 0
tomato_count = 0

bfs()
if not tomato_count:
    print(result)
else:
    print(-1)
