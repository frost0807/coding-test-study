"""
해당 문제는 크기가 8x8 이므로 벽을 설치할수 있는 모든 조합의 수는 최악의 경우도 100,000보다 작은수
문제 풀이: 풀이 아이디어 벽을 설치할수 있는 모든 조합의 경우의 수를 구해서 안전지대 값을 계산하는 처리
    1.벽을 설치후 감염 공간을 만드는 함수 DFS
    2.안전지대 구하는 함수 
    3.경우의 수를 조합 DFS
"""
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())

# 그래프
data = [list(map(int, input().split())) for _ in range(n)]
# 가벽이 설치된 그래프
temp = [[0]*m for _ in range(n)]

# 결과값 저장
result = 0

dx = [0, 0, -1, 1]  # 상하좌우
dy = [1, -1, 0, 0]  # 상하좌우


# 바이러스 퍼짐
def dfs_virus(x, y):
    # 상하좌우 어디든 갈수 있다.
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        # 빈 공간이면
        if 0 <= tx and tx < n and 0 <= ty and ty < m:
            if temp[tx][ty] == 0:
                temp[tx][ty] = 2
                dfs_virus(tx, ty)

# 안전 지대 계산 바이러스 퍼지고 계산


def get_safezone():
    temp_result = 0
    for row in temp:
        temp_result += row.count(0)
    # for i in range(n):
    #     for j in range(m):
    #         if temp[i][j] == 0:
    #             temp_result += 1
    return temp_result


def dfs_block(count):
    # 종료 시점
    global result
    if count == 3:
        for a in range(n):
            for b in range(m):
                temp[a][b] = data[a][b]

        for a in range(n):
            for b in range(m):
                if temp[a][b] == 2:
                    dfs_virus(a, b)

        result = max(result, get_safezone())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs_block(count)
                data[i][j] = 0
                count -= 1


dfs_block(0)
print(result)
