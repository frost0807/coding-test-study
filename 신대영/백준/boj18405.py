from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # N X M 행렬

graph = []
virus_data = []
for i in range(n):
    temp_list = list(map(int, input().split()))
    graph.append(temp_list)

    for t in range(n):
        if temp_list[t] != 0:
            virus_data.append([temp_list[t], 0, i, t,])

s, x, y = map(int, input().split())

# 상하좌우 처리
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 숫자가 낮은것 부터 처리
virus_data.sort()
queue = deque(virus_data)

while queue:
    virus_num, s_1, x_1, y_1 = queue.popleft()

    if s_1 == s:
        break

    for i in range(4):
        tx = x_1 + dx[i]
        ty = y_1 + dy[i]
        if 0 <= tx < n and 0 <= ty < n:
            if graph[tx][ty] == 0:
                graph[tx][ty] = virus_num
                queue.append([virus_num, s_1 + 1, tx, ty])

print(graph[x - 1][y - 1])

# # 바이러스 퍼지는 함수
# def virus(virus_num):
#     # global x, y, answer

#     # 요청하는 좌표가 됬으면 끝
#     # if a_x == x and a_y == y:
#     #     answer = virus_num
#     #     return
#     # print(temp_list[virus_num])
#     temp = []
#     for tl in temp_list[virus_num]:
#         for i in range(4):
#             tx = tl[0] + dx[i]
#             ty = tl[1] + dy[i]
#             if 0 <= tx < n and 0 <= ty < n:
#                 if data[tx][ty] == 0:
#                     data[tx][ty] = virus_num
#                     temp.append([tx, ty])

#     temp_list[virus_num] = copy.deepcopy(temp)
#     # print(temp_list[virus_num])

# # 1,2,3의 위치를 찾는 함수


# def init_virus():
#     for i in range(n):
#         for j in range(n):
#             for c in range(1, k + 1):
#                 if data[i][j] == c:
#                     temp_list[c].append([i, j])


# init_virus()

# for _ in range(s):
#     for i in range(1, k+1):
#         virus(i)

# answer = data[x - 1][y - 1]
