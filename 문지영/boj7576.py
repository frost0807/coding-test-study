"""
bfs

참고: https://velog.io/@hysong/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
"""
from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split()) # 순서 주의
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

queue = deque()
def BFS():  # 큐에는 익은 토마토가 들어있음
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        now = queue.popleft()
        for k in range(4):
            x, y = now[0] + dx[k], now[1] + dy[k]
            if 0 <= x < N and 0 <= y < M:
                if board[x][y] == 0:
                    board[x][y] = board[now[0]][now[1]] + 1  # 익은 날짜+1 저장
                    queue.append((x, y))

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            queue.append((i, j))  # 익은 토마토 큐에 삽입

BFS()
if any(0 in r for r in board): print(-1)  # 모두 익지 못함 예외 처리
else: print(max(map(max, board)) - 1) # 최소 날짜
