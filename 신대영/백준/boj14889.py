from itertools import combinations, permutations
import sys
input = sys.stdin.readline


def get_total(n_list):
    tmp_result = 0
    for a in list(permutations(n_list, 2)):
        tmp_result += data[a[0]][a[1]]

    return tmp_result


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
nums = [i for i in range(N)]
result = 1e9

for a in list(combinations(nums, N//2)):
    b = list(set(nums) - set(a))
    result = min(result, abs(get_total(a) - get_total(b)))

print(result)
