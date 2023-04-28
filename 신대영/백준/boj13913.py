from collections import deque


def bfs():
    global N, K, MAX
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()

        if x == K:
            print(dist[x])
            result = []
            while x != N:
                result.append(x)
                x = path[x]
            result.append(N)
            print(*result[::-1])
            return
        for tx in (x-1, x+1, x*2):
            if 0 <= tx <= MAX and not dist[tx]:
                dist[tx] = dist[x] + 1
                path[tx] = x
                queue.append(tx)


N, K = map(int, input().split())
MAX = 100000
dist = [0] * (MAX + 1)
path = [0] * (MAX + 1)

bfs()
