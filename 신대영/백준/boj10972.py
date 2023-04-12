import sys
from itertools import permutations
n = int(input())
# 메모리 초과
input = sys.stdin.readline

n = int(input())
nums = [i for i in range(1, n + 1)]
num_case = tuple(map(int, input().split()))
result = tuple('-1')
perms = list(permutations(nums, n))

for i, v in enumerate(perms):
    if num_case == v:
        if i + 1 != len(perms):
            result = perms[i+1]

        break

print(*result)


# 베스트 풀이
nums = list(map(int, input().split()))

result = []

for i in range(n - 1, 0, -1):  # 뒤에서부터 비교
    if nums[i - 1] < nums[i]:  # 앞에 수가 뒤에 수보다 작다면
        for j in range(n - 1, 0, -1):  # 다시 그 앞에 값을 맨 뒤값과 비교
            if nums[i - 1] < nums[j]:
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                result = nums[:i] + sorted(nums[i:])
                print(*result)
                exit()

print(-1)
