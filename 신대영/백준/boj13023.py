import sys
input = sys.stdin.readline


def set_grapth():
    """
    각 지점에서 연결되어 있는 지점을 2차원 배월로 초기화하는 함수
    """
    global M, N
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


def dfs(n, depth):
    """
    각 지점에서 연결되어 있는 지점으로 깊이우선 탐색으로 찾는 함수
    parameter: n = 현재 지점, depth = 탐색 깊이
    """
    global result
    if depth == 5:  # 탐색 깊이가 5개 되면 종료
        result = 1  # 1 출력
        return

    # 각 지점에 연결되어 있는 지점 루프 돌면서 탐색
    for i in graph[n]:
        if not visited[i] and not result:  # 방문하지 않은 지점과 아직 탐색이 종료가 되지 않았으면 처리
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False


N, M = map(int, input().split())
graph = [list() for _ in range(N)]
visited = [False] * N
result = 0
set_grapth()

# 각 지점별로 전부 탐색 처리
for i in range(N):
    if not result:
        visited[i] == True
        dfs(i, 0)
        visited[i] == False

print(result)
