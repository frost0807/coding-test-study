# bfs로 문제 풀이
from collections import deque

N, L, R = map(int, input().split())
# 2차원 그래프에 담아서 처리
graph = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = False

answer = 0


def bfs(x, y, visited):
    global flag, N, R, L

    queue = deque()
    queue.append((x, y))

    temp = []
    temp.append((x, y))

    visited[x][y] = True
    total = graph[x][y]
    count = 1

    while queue:
        px, py = queue.popleft()

        for i in range(4):
            tx = px + dx[i]
            ty = py + dy[i]

            if 0 <= tx < N and 0 <= ty < N and not visited[tx][ty] and L <= abs(graph[px][py] - graph[tx][ty]) <= R:
                temp.append((tx, ty))
                queue.append((tx, ty))
                visited[tx][ty] = True
                total += graph[tx][ty]
                count += 1

    if count > 1:
        flag = True
        mv_p = total / count

        for x, y in temp:
            graph[x][y] = mv_p

    print(graph)


while True:
    flag = False
    # 해당위치 연합 index 저장
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, visited)

    if not flag:
        break

    answer += 1


print(answer)
