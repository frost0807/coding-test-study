# 라이브러리 사용
from itertools import permutations

n = int(input())
nums = [i for i in range(1, n+1)]

for a in list(permutations(nums, n)):
    print(*a)

# dfs로 문제 풀이
n = int(input())
nums = [i for i in range(1, n+1)]

visited = [False] * n

result = []


def dfs(depth):
    global n
    if depth == n:
        print(*result)
        return

    for i in range(len(nums)):
        if not visited[i]:
            result.append(nums[i])
            visited[i] = True
            dfs(depth + 1)
            result.pop()
            visited[i] = False


dfs(0)
