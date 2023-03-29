# 행렬의 수
import copy
from itertools import combinations

# N = int(input())
# block = 3

# t_a = []
# graph = []
# # 2차원 행렬 초기화 및 선생님 위치 저장
# for i in range(N):
#     dt = list(map(str, input().split()))
#     graph.append(dt)
#     # 선생님 위치 저정
#     for idx, j in enumerate(dt):
#         if j == 'T':
#             t_a.append((i, idx))

# tx = [-1, 1, 0, 0]
# ty = [0, 0, -1, 1]

# # 선생님 찾기


# def teacher_block(x, y):
#     global block
#     # 상
#     if x > 0:
#         for i in range(1, N):
#             ux = x - i
#             if ux < 0 or graph[ux][y] in ('O', 'T'):
#                 break

#             if graph[ux][y] == 'S':
#                 if graph[ux + 1][y] == 'X':
#                     graph[ux + 1][y] = 'O'
#                     block -= 1
#                 elif graph[ux + 1][y] == 'T':
#                     block = -1

#                 break

#     # 하
#     elif x < N:
#         for i in range(1, N):
#             dx = x + i

#             if dx < 0 or graph[dx][y] in ('O', 'T'):
#                 break

#             if graph[dx][y] == 'S':
#                 if graph[dx - 1][y] == 'X':
#                     graph[dx - 1][y] = 'O'
#                     block -= 1
#                 elif graph[dx - 1][y] == 'T':
#                     block = -1

#                 break

#     # 좌
#     if y > 0:
#         for i in range(1, N):
#             ly = y - i

#             if ly < 0 or graph[x][ly] in ('O', 'T'):
#                 break

#             if graph[x][ly] == 'S':
#                 if graph[x][ly + 1] == 'X':
#                     graph[x][ly + 1] = 'O'
#                     block -= 1
#                 elif graph[x][ly + 1] == 'T':
#                     block = -1

#                 break

#     # 우
#     elif y < N:
#         for i in range(1, N):
#             ry = y + i

#             if ry < 0 or graph[x][ry] in ('O', 'T'):
#                 break

#             if graph[x][ry] == 'S':
#                 if graph[x][ry - 1] == 'X':
#                     graph[x][ry - 1] = 'O'
#                     block -= 1
#                 elif graph[x][ry - 1] == 'T':
#                     block = -1

#                 break


# for x, y in t_a:
#     if block < 0:
#         break
#     else:
#         teacher_block(x, y)

# # print(block)
# # for ss in [' '.join(x) for x in graph]:
# #     print(ss)
# # 상하좌우 다 확인
# if block < 0:
#     print('NO')
# else:
#     print('YES')


# 행렬의 수
import sys
input = sys.stdin.readline
N = int(input())
block = 3

t_t = []
t_x = []
graph = []
# 2차원 행렬 초기화 및 선생님 위치 저장
for i in range(N):
    dt = list(map(str, input().rstrip().split()))
    graph.append(dt)
    # 선생님 위치 저정
    for idx, j in enumerate(dt):
        if j == 'T':
            t_t.append((i, idx))
        elif j == 'X':
            t_x.append((i, idx))


is_check = []


def dfs(x, y, temp_graph, n):
    global block, is_success, is_check

    for i in range(1, N):
        ux = x - i
        if ux < 0 or temp_graph[ux][y] in ('O', 'T'):
            break

        if temp_graph[ux][y] == 'S':
            is_check[n] = 1
            return

    for i in range(1, N):
        dx = x + i

        if dx >= N or temp_graph[dx][y] in ('O', 'T'):
            break

        if temp_graph[dx][y] == 'S':
            is_check[n] = 1
            return
    # 좌우
    for i in range(1, N):
        ly = y - i

        if ly < 0 or temp_graph[x][ly] in ('O', 'T'):
            break

        if temp_graph[x][ly] == 'S':
            is_check[n] = 1
            return

    for i in range(1, N):
        ry = y + i

        if ry >= N or temp_graph[x][ry] in ('O', 'T'):
            break

        if temp_graph[x][ry] == 'S':
            is_check[n] = 1
            return


for comb in list(combinations(t_x, block)):
    temp_graph = copy.deepcopy(graph)
    is_check = [0] * len(t_t)
    for c in comb:
        temp_graph[c[0]][c[1]] = 'O'

    for i in range(len(t_t)):
        dfs(t_t[i][0], t_t[i][1], temp_graph, i)

    if sum(is_check) == 0:
        break

# 상하좌우 다 확인
if sum(is_check) == 0:
    print('YES')
else:
    print('NO')
