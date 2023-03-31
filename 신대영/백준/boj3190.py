# 런타임 에러 발생
# from collections import deque

# N = int(input())
# K = int(input())

# graph = [['X'] * N for _ in range(N)]

# # 사과 위치 지정
# for _ in range(K):
#     x,y = map(int, input().split())
#     graph[x-1][y-1] = 'A'

# # 방향전환 정보
# L = int(input())
# L_dict = {}

# for _ in range(L):
#     x,c = map(str,input().split())
#     L_dict[int(x)] = c

# direct_chg = {'left':{'L':'down', 'D':'up'},
#         'right':{'L':'up', 'D':'down'},
#         'up':{'L':'left', 'D':'right'},
#         'down':{'L':'right', 'D':'left'}}
# direct = {'left': (0, -1), 'right': (0, 1), 'up':(-1,0), 'down':(1,0)}

# sdeque = deque()

# result = 0

# def dfs(d,x,y):
#     global result, L, N, K

#     # 움직이는 방향에 따른 x,y 설정
#     if result in L_dict:
#         d = direct_chg[d][L_dict[result]]

#     ax,ay = direct[d]
#     dx = x + ax
#     dy = y + ay

#     result += 1
#     sdeque.append((x,y))

#     # 벽을 만났을 경우
#     if dx < 0 or N <= dx or dy < 0 or N <= dy or (dx,dy) in sdeque:
#         return
#     else:
#         # 비어있는 공간이면 재귀 다시 호출
#         # 꼬리에 닿으면 종료
#         if graph[dx][dy] == 'X':
#             sdeque.popleft()

#         dfs(d,dx,dy)

# dfs('right',0,0)
# print(result)

# 베스트 풀이
from collections import deque


def change(d, c):
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전: 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
    # 왼쪽 회전: 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1 방향
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def start():
    direction = 1  # 초기 방향
    time = 1  # 시간
    y, x = 0, 0  # 초기 뱀 위치
    visited = deque([[y, x]])  # 방문 위치
    arr[y][x] = 2
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
            if not arr[y][x] == 1:  # 사과가 없는 경우
                temp_y, temp_x = visited.popleft()
                arr[temp_y][temp_x] = 0  # 꼬리 제거
            arr[y][x] = 2
            visited.append([y, x])
            if time in times.keys():
                direction = change(direction, times[time])
            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time


if __name__ == "__main__":

    # input
    N = int(input())
    K = int(input())
    arr = [[0] * N for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a - 1][b - 1] = 1  # 사과 저장
    L = int(input())
    times = {}
    for i in range(L):
        X, C = input().split()
        times[int(X)] = C
    print(start())
