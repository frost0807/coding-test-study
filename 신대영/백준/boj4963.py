import sys
sys.setrecursionlimit(10**6)
distx = [0, -1, 1, 0, -1, 1, -1, 1]
disty = [-1, -1, -1, 1, 1, 1, 0, 0]


def dfs(x, y):
    """
        dfs 런타임 에러 (RecursionError) 발생 해결 
          -> sys.setrecursionlimit(10**6) 추가
    """
    for i in range(8):
        tx = x + distx[i]
        ty = y + disty[i]

        if 0 <= tx < H and 0 <= ty < W and graph[tx][ty] == 1:
            graph[tx][ty] = 0
            dfs(tx, ty)


def bfs(x, y):
    """
        bfs로 풀이
    """
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            tx = x + distx[i]
            ty = y + disty[i]

            if 0 <= tx < H and 0 <= ty < W and graph[tx][ty] == 1:
                graph[tx][ty] = 0
                queue.append((tx, ty))


while True:
    W, H = map(int, input().split())

    # 종료
    if W == 0 and H == 0:
        break

    result = 0
    # graph 생성
    graph = [list(map(int, input().split())) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1:
                result += 1
                graph[i][j] = 0
                dfs(i, j)
                # bfs(i, j)
    print(result)
