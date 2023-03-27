# 순열 라이브러리로 풀시 시간초과
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(str, input().split()))
buho_count = list(map(int, input().split()))
buho = ['+', '-', '*', '//']
buho_list = []
max_res = -1e9
min_res = 1e9

for i in range(len(buho_count)):
    buho_list += ([buho[i]] * buho_count[i])

for p in list(permutations(buho_list, n - 1)):
    result = nums[0]
    for i in range(1, n):
        if int(result) < 0 and p[i-1] == '//':
            result = -eval(str(-result) + p[i-1] + nums[i])
        else:
            result = eval(str(result) + p[i-1] + nums[i])

    max_res = max(max_res, result)
    min_res = min(min_res, result)

print(max_res)
print(min_res)

##
n = int(input())
nums = list(map(str, input().split()))
plus, minus, multi, div = map(int, input().split())
max_res = -1e9
min_res = 1e9


# DFS로 문제 폴어서 완료
def dfs(depth, total):
    # 종료 시점 경우의 수 완료
    if depth == n:
        max_res = max(max_res, total)
        min_res = min(min_res, total)
        return

    if plus > 0:
        plus -= 1
        dfs(depth + 1, total + nums[depth])
        plus += 1
    if minus > 0:
        minus -= 1
        dfs(depth + 1, total - nums[depth])
        minus += 1
    if multi > 0:
        multi -= 1
        dfs(depth + 1, total * nums[depth])
        multi += 1
    if div > 0:
        multi -= 1
        dfs(depth + 1, -(-total // nums[depth])
            if total < 0 else total // nums[depth])
        multi += 1


dfs(0, 0)
print(max_res)
print(min_res)
