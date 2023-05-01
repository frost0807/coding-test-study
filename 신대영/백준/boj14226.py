from collections import deque
S = int(input())  # 이모티콘 개수

visited = [[-1] * (S+1) for _ in range(S+1)]


def bfs():
    queue = deque()
    queue.append((1, 0))  # 화면 이모티콘수 클립보드 이모티콘수
    visited[1][0] = 0

    while queue:
        e, c = queue.popleft()

        # 화면에 있는 이모티콘 클립보드에 복사
        if visited[e][e] == -1:
            visited[e][e] = visited[e][c] + 1
            queue.append((e, e))

        # 클립보드에 있으면 존재하면 화면에 붙여넣기
        if e + c <= S and visited[e+c][c] == -1:
            visited[e+c][c] = visited[e][c] + 1
            queue.append((e+c, c))
        # 화면 이모티콘 삭제
        if e - 1 >= 0 and visited[e-1][c] == -1:
            visited[e-1][c] = visited[e][c] + 1
            queue.append((e-1, c))


bfs()

result = visited[S][1]

for i in range(1, S):
    if visited[S][i] != -1:
        result = min(result, visited[S][i])
print(result)
