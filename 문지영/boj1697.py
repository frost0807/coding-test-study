"""
bfs

참고: https://chancoding.tistory.com/193
"""

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100000  # N,K의 최대위치
arr = [0] * (MAX + 1)  # 걸리는 시간


def BFS(i):
    queue = deque([i])

    while queue:
        now = queue.popleft()
        if now == K:  # 동생 위치
            break
        for x in [now - 1, now + 1, now * 2]:  # 이동할 위치
            if 0 <= x <= MAX:
                if not arr[x]:
                    arr[x] = arr[now] + 1  # 현재+1초 시간
                    queue.append(x)
    print(arr[K])

BFS(N)