from collections import deque


def bfs():
    global N, K, MAX
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()

        if x == K:
            print(dist[x])
            break
        for tx in (x*2, x-1, x+1):
            if 0 <= tx <= MAX and not dist[tx]:
                dist[tx] = dist[x] + (0 if x*2 == tx else 1)
                queue.append(tx)


N, K = map(int, input().split())
MAX = 100000
dist = [0] * (MAX + 1)

bfs()
