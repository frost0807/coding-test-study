import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(str, input())) for _ in range(N)]
dangi_count = []
dist = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def dfs(x, y, d_idx):

    for tx, ty in dist:
        dx = x + tx
        dy = y + ty

        if 0 <= dx < N and 0 <= dy < N and graph[dx][dy] == '1':
            dangi_count[d_idx] += 1
            graph[dx][dy] = '0'
            dfs(dx, dy, d_idx)


for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            dangi_count.append(1)
            graph[i][j] = '0'
            dfs(i, j, len(dangi_count) - 1)

dangi_count.sort()
print(len(dangi_count))
print('\n'.join(map(str, dangi_count)))
