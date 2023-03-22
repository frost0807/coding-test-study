"""
문제유형: 완전탐색
문제링크: https://www.acmicpc.net/problem/15686
"""
from itertools import combinations
import sys
INF = sys.maxsize
input = sys.stdin.readline
n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

c_list = []  # 치킨집 위치
h_list = []  # 집 위치
answer = INF

# 완전탐색으로 치킨집 위치 집 위치 저장
for i, a in enumerate(g):
    for j, b in enumerate(a):
        if b == 2:
            c_list.append([i, j])
        elif b == 1:
            h_list.append([i, j])


def getMinDistanceSum(chicken):
    sum_dis = []
    for H in h_list:
        dis_t = INF
        for d in chicken:
            dis_t = min(dis_t, abs(d[0] - H[0]) + abs(d[1] - H[1]))

        sum_dis.append(dis_t)
    answer = min(answer, sum(sum_dis))


# 최소 거리 리턴
for C in list(combinations(c_list, m)):
    getMinDistanceSum(C)

print(answer)
