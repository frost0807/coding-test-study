
def dfs(depth, x, y, color, sx, sy):
    """
    게임판에서 좌우상하 각 좌표 깊이 우선 탐색 함수
    parameter:
        depth : 깊이(개수)
        x : 현재 x좌표
        y : 현재 y좌표
        color : 게임판 색상
        sx : 시작 x좌표
        sy : 시작 y좌표
    """
    global is_cycle

    if is_cycle:  # 이미 사이클이 완료되면 리턴
        return

    if x == sx and y == sy and depth >= 4:  # 현재 좌표가 시작 좌표와 동일하고 개수가 4보다 클때 사이클 완료 리턴
        is_cycle = True
        return

    for dx, dy in dist:  # 좌우상하 루프돌면서 처리
        tx = x + dx
        ty = y + dy

        # 이동하는 좌표가 게임판 안에 있어야 하며 이동좌표에 색상이 일치하고 방문하지 않은 곳이면 처리
        if 0 <= tx < N and 0 <= ty < M and graph[tx][ty] == color and not visited[tx][ty]:
            visited[tx][ty] = True
            dfs(depth + 1, tx, ty, color, sx, sy)
            visited[tx][ty] = False


N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]  # NxM 게임판
visited = [[False] * M for _ in range(N)]  # 방문여부 체크
dist = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 좌우상하 이동 좌표
is_cycle = False  # 사이클여부

# 모든 좌표 돌면서 처리
for i in range(N):
    for j in range(M):
        dfs(0, i, j, graph[i][j], i, j)

print('Yes' if is_cycle else 'No')
