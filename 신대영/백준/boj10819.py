from itertools import permutations


def div_sum(num_list):
    d_sum = 0
    for i in range(1, len(num_list)):
        d_sum += abs(num_list[i-1] - num_list[i])

    return d_sum


n = int(input())
nums = list(map(int, input().split()))
result = 0

for a in list(permutations(nums, len(nums))):
    result = max(result, div_sum(a))

print(result)
